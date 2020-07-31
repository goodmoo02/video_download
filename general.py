import subprocess
import utils
import requests
from bs4 import BeautifulSoup
import streamlink

def youtube_download(url, direc=""):
    '''
    유튜브 영상 or 유튜브 채널 or 재생목록(playlist) 동영상 전체 다운로드 ('bestvideo+bestaudio')
    (youtube video or youtube channel or playlist videos download with 'bestvideo+bestaudio')
    재생목록은 공개 시에만 다운로드 가능
    (Download available when playlist is opend not private)

    :param   url: 유튜브 채널 or 재생목록 주소  (youtube_channel or playlist url)
           direc: 다운로드할 디렉토리           (download directory)
    '''

    ## download youtube-dl.exe ##
    utils.download_youtube_dl(direc)

    ## if download channel or playlist videos and no option direc, use title for directory name
    if ("/channel/" or "/playlist?list=" in url) and direc == "":
        res = requests.get(url)
        bs_html = BeautifulSoup(res.text, "html.parser")
        direc = bs_html.find('meta', {'name':'title'}).get("content")


    ## use youtube-dl with subprocess
    youtube_dl_process = subprocess.check_output(['youtube-dl', '-f', 'bestvideo+bestaudio', '-ciw', '-o', direc + "/%(title)s.%(ext)s", '-v', url], shell=True, encoding='euc-kr', errors='replace')
    print(youtube_dl_process)



def stream_download(url, name=""):
    '''
    download streaming video in
    :param  url: stream_url
           name: file_name
    '''

    ## default directory ##
    dir_name = "."

    ## classify stream services ##
    # TWITCH TV #
    if "twitch" in url:
        split_list = url.split('/')
        dir_name = split_list[split_list.index("www.twitch.tv") + 1]
        if name == "":
            name = split_list[split_list.index("www.twitch.tv") + 1]
            print(name)
    # afreecatv #
    elif "afreecatv" in url:
        res = requests.get(url)
        bs_html = BeautifulSoup(res.text, "html.parser")
        dir_name = bs_html.find('div', {"class": "nickname"}).get_text()
        if name == "":
            name = bs_html.find('meta', {'property': 'og:title'}).get("content")
    # huya.com #
    elif "huya" in url:
        res = requests.get(url)
        bs_html = BeautifulSoup(res.text, "html.parser")
        print(bs_html)
        dir_name = bs_html.find("h3", {"class": "host-name"}).get_text()
        if name == "":
            name = bs_html.find("div", {"class": "host-title"}).h1.get_text()

    ## API streamlink search streaming video url(maybe m3u8 address)
    stream_url = streamlink.streams(url)['best'].url
    print(stream_url)

    ## use ffmpeg with subprocess
    subprocess.call(["ffmpeg", "-i", stream_url, "-c", "copy", dir_name + "/" + name + '.mkv'])


if __name__ == '__main__':
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='command your website')
    parser.add_argument("service",
                        metavar="<service>",
                        help="command 'youtube' or 'stream'")

    parser.add_argument("--url",
                        metavar="<url>",
                        help="'website'")

    parser.add_argument('--name', required=False,
                        default=".",
                        metavar="<name>",
                        help="directory or file name")
    args = parser.parse_args()

    # Validate arguments
    url = args.url
    name = args.name
    if args.service == "youtube":
        print("youtube")
        youtube_download(url, name)
    elif args.service == "stream":
        print("stream")
        stream_download(url, name)
