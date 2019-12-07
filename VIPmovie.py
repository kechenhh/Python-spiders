
from multiprocessing import Pool
import requests
import os


def download(i, URL):
    url = URL + '%04d.ts'% i
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        content = response.content
        with open('./{}'.format(url[-10:]), 'wb') as f:
            f.write(content)
    except IndexError:
        pass


def main(URL, n1, n2):

    pool = Pool(30)
    for i in range(n1, n2 + 1):
        # 执行任务
        pool.apply_async(download, (i, URL))
    pool.close()
    pool.join()


if __name__ == '__main__':
    # 创建一个进程池，同时执行20个任务
    print("http://www.vip1280.cn/")
    print("需要输入的链接类似:https://dapian.video-yongjiu.com/20190912/11666_d6886bb2/1000k/hls/7d56f9697fa00")
    URL = input('输入链接：')
    n1 = input('输入ts开始个数：')
    n2 = input('输入ts结束个数：')
    n1 = int(n1)
    n2 = int(n2)
    main(URL, n1, n2)
    print("下载结束")
    title = URL[-10:] + '--' + str(n1) + '-' + str(n2)
    os.system('copy /b *.ts {}.mp4'.format(title))
    os.system('del *.ts')
