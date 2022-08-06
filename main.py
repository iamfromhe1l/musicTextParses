import requests
from bs4 import BeautifulSoup as bs

def getTextUrls(mainUrl):
    result = []
    urls = [f'{mainUrl}/ru/grazgdanskaya-oborona-grob/']
    for elem in [f'{mainUrl}/ru/grazgdanskaya-oborona-grob/index-p{i}.html' for i in range(1,6)]: urls.append(elem)
    for url in urls:
        res = requests.get(url)
        body = bs(res.text, 'lxml')
        for elem in [mainUrl + elem['href'] for elem in body.find_all('table', class_='itemlist')[0].find_all('a')]: result.append(elem)
    return result

def getTextFromUrl(urls):
    texts = []
    for url in urls:
        res = requests.get(url)
        body = bs(res.text, 'lxml')
        text = body.find('p', id='textpesni').text
        texts.append([url.split('/')[-1].split('.')[0],text])
    return texts

def textToFile(texts):
    for text in texts:
        with open(f'musicTexts/{text[0]}.txt', 'w', encoding='utf-8') as f:
            f.write(text[1])

def main():
    mainUrl = 'http://lyricshare.net'
    urlArr = getTextUrls(mainUrl)
    texts = getTextFromUrl(urlArr)
    textToFile(texts)
    

if __name__ == '__main__':
    main()