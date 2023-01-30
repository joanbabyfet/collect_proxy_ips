import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://free-proxy-list.net'
    resp = requests.get(url)
    resp.encoding = 'utf-8' # 使用与网页相对应的编码格式, 避免乱码
    soup = BeautifulSoup(resp.text, 'html.parser') # 通过html dom解析器采集数据
    
    proxy_list = soup.select_one('textarea').text.splitlines() # 返回列表类型
    temp = []
    for k, v in enumerate(proxy_list):
        if k > 2 and v != '': # 干掉非ip或空字符串
            temp.append(v)
    content = '\n'.join(temp) # 列表转字符串

    # 将整个字符串内容写入txt文件
    f = open('proxy.txt', 'w')
    f.write(content)
    f.close()

if __name__ == '__main__': # 主入口
    main()