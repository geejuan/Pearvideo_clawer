import requests


class Pearvideo_clawer:
    def __init__(self, url):
        self.url = url
        self.contId = url.split('_')[1]  # 拿到contId
        self.Hearder = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/90.0.4430.85 Safari/537.36 ',
            # 防盗链: 溯源， 本次请求的上一级页面
            'Referer': url
        }
        self.videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={self.contId}&mrd=0.3503403469300008'
        # 对srcURL里面的内容进行修正

    def Clawer(self):
        resp = requests.get(self.videoStatusUrl, headers=self.Hearder)
        dic = resp.json()  # 拿到videoStatus返回的json. -> srcURL
        srcUrl = dic['videoInfo']['videos']['srcUrl']
        systemTime = dic['systemTime']
        self.srcUrl = srcUrl.replace(systemTime, f'cont-{self.contId}')

    def Download(self):
        with open(f'{self.contId}.mp4', 'wb') as f:
            f.write(requests.get(self.srcUrl).content)


if __name__ == '__main__':
    URL = input('请输入视频链接')
    clawer = Pearvideo_clawer(URL)
    clawer.Clawer()
    clawer.Download()
    print('over')
