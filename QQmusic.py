import requests
import json
from urllib.request import urlretrieve
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

def main(url,song_id,song_url):
    r =requests.get(url,headers=headers)
    html = r.text
    json_obj = json.loads(html)
    sip = json_obj['req_0']['data']['sip'][0]
    purl = json_obj['req_0']['data']['midurlinfo'][0]['purl']

    r1 = requests.get(song_url, headers=headers)
    res_xpath = etree.HTML(r1.text)

    song_title = res_xpath.xpath('//h1/text()')[0]
    songer = res_xpath.xpath('//div[@class="data__singer"]/@title')[0]

    download_url = sip+purl
    urlretrieve(download_url, song_title+'-'+songer+'.mp3')

if __name__ == '__main__':
    print("实例URL:https://y.qq.com/n/yqq/song/003uw9dp2HcDl2.html")
    song_url = input("输入歌曲URL:")
    song_url1 = song_url.replace('https://y.qq.com/n/yqq/song/','')
    song_id = song_url1.replace('.html', '')

    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7743664995","songmid":["'+str(song_id)+'"],"songtype":[0],"uin":"923407526","loginflag":1,"platform":"20"}}}'
    main(url,song_id,song_url)


