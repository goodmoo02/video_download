from requests import get
import os

## url 다운로드 함수 ##
def download(url, name, ext, direc="."):
    '''
    :param url: url to download
    :param name: file_name
    :param ext: file_extension
    :param direc: download directory
    :return: download file with name.ext in directory
    '''
    down_name = direc + "/" + name + "." + ext
    with open(down_name, "wb") as file:
        response = get(url)
        print(response)
        file.write(response.content)
        if "200" in str(response):
            print("완료: " + down_name)
        else:
            print("다운로드 실패:" + down_name)



def download_youtube_dl(direc="."):
    '''
    :param direc: download directory
    :return: downlaod youtube-dl.exe in directory
    '''
    if os.path.isfile("youtube-dl.exe"):
        print("already youtube-dl.exe exists")
    else:
        download(name="youtube-dl", ext="exe",direc=direc)