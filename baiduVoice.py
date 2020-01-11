from aip import AipSpeech
#pip install baidu_aip
#百度语音合成

app_id = '17062694'
api_key = 'g7l69R8N7GdAZTAZjEhIrCgA'
secret_key = 'wdspTuGP7LyztSSNHK79UY9MEs57Koy6'

client = AipSpeech(app_id, api_key, secret_key)
#读取当前目录下名为"test.txt"的文件
with open(r"./test.txt", 'r',encoding='utf-8') as t:
    text = t.read()
    result = client.synthesis(text, "zh", 1, {
        "vol": 9, #音量
        "spd": 4, #语速
        "pit": 7, #音调
        "per": 4, #音色
    })
    if not isinstance(result, dict):
        #保存为"合成.mp3"
        with open('合成.mp3', 'wb') as f:
            f.write(result)
    else:
        print(result)
