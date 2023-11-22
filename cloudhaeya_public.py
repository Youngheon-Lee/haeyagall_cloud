# moduel import
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
from collections import Counter

import matplotlib.pyplot as plt

#위에 없는 모듈은 pip으로 다 받으셔야 합니다

#일단은 디씨글을 읽도록 세팅되어 있지만 여러모로 응용 가능
BASE_URL = "https://gall.dcinside.com/board/lists"

#본인이 사용할 폴더를 지정 (아래 경로는 임의로 지정한겁니다)
destFile = r"c:\code\haeyagall_cloud\title_con.txt"
fw = open('title_con.txt','w', encoding='utf-8')
fw.close()

#1~30페이지까지 디폴트 세팅되어 있지만 변경 가능합니다. 하지만 너무 많이 긁으면 중간에 짤리는 경우 있음ㅠ
for i in range(1,31):

    # 파라미터 설정
    
    params = {
            'id': 'baseball_ab2','page':i}
    # 헤더 설정 (유저에이전트에 본인 브라우저 세팅을 넣어주세요)
    headers={
                    'User-Agent' : '본인의유저에이전트' 
                }
    req = requests.get(BASE_URL, params=params, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')    
    article_list = soup.find('tbody').find_all('tr')
    

    for tr_item in article_list:

        title_tag = tr_item.find('a', href=True)
        title = title_tag.text
        with open(destFile,'a', encoding='utf-8') as f:
            f.write(' '+title)
            
text = open('title_con.txt', encoding='utf-8').read()


#이하는 쓸데없이 긁어지는 내용을 방지하는 키워드 리스트입니다. 김유식이 자꾸 이상한 뭔뭔 스타는 이딴글 써놔서 많이 길어짐... 임의로 세팅하시면 됩니다.
stopwords = set(STOPWORDS)
stopwords.add('학폭')
stopwords.add('논란')
stopwords.add('절대')
stopwords.add('가기')
stopwords.add('것')
stopwords.add('보러')
stopwords.add('방송')
stopwords.add('특별')
stopwords.add('스타는')
stopwords.add('열정만큼')
stopwords.add('아름다운')
stopwords.add('개야갤')
stopwords.add('진짜')
stopwords.add('씨발')
stopwords.add('시발')
stopwords.add('니케')
stopwords.add('1주년')
stopwords.add('이벤트')
stopwords.add('해외야구')
stopwords.add('갤러리')
stopwords.add('이용')
stopwords.add('같은')
stopwords.add('결혼과')
stopwords.add('연애하기')
stopwords.add('싫어지게')
stopwords.add('만드는')
stopwords.add('예능')
stopwords.add('프로그램은')
stopwords.add('세계')
stopwords.add('최초')
stopwords.add('EPL')
stopwords.add('구단과')
stopwords.add('함께하는')
stopwords.add('POP-UP')
stopwords.add('오픈')
stopwords.add('안내 게시물')
stopwords.add('아티스트가 되고')
stopwords.add('오픈 클레이와')
stopwords.add('사이트 관리자')
stopwords.add('관리자 모집')
stopwords.add('발행 오픈')
stopwords.add('오픈 안내')
stopwords.add('국제결혼 선택하길')
stopwords.add('ㅋㅋㅋㅋㅋ')
stopwords.add('ㅋㅋㅋㅋ')
stopwords.add('ㅋㅋ')
stopwords.add('ㅋㅋㅋㅋㅋㅋ')
stopwords.add('되고 싶어요')
stopwords.add('오픈 안내')
stopwords.add('발행 오픈')
stopwords.add('오픈 클레이와')
stopwords.add('ㅋㅋㅋ')
stopwords.add('아티스트')
stopwords.add('tripleS')
stopwords.add('채연')
stopwords.add('빛나는')
stopwords.add('뭔지')
stopwords.add('jpg')
stopwords.add('모바일에서도')
stopwords.add('UP')
stopwords.add('서비스')
stopwords.add('POP')
stopwords.add('디시')
stopwords.add('AI')
stopwords.add('갤러리')
stopwords.add('클레이')
stopwords.add('아티스트')
stopwords.add('발행')
stopwords.add('게시물')
stopwords.add('드라마처럼')
stopwords.add('우여곡절이')
stopwords.add('근데')
stopwords.add('그냥')
stopwords.add('사기를')
stopwords.add('맞아도')
stopwords.add('이상하지')
stopwords.add('않을')
stopwords.add('결혼으로')
stopwords.add('인생이')
stopwords.add('변한')
stopwords.add('것')
stopwords.add('gif')
stopwords.add('webp')
stopwords.add('이유')
stopwords.add('오늘')
stopwords.add('속보')
stopwords.add('근황')
stopwords.add('실시간')
stopwords.add('존나')
stopwords.add('이')
stopwords.add('이거')
stopwords.add('왜')
stopwords.add('요즘')
stopwords.add('다')
stopwords.add('아닌지')
stopwords.add('아니')
stopwords.add('은근')
stopwords.add('2024')
stopwords.add('개추')
stopwords.add('레전드')
stopwords.add('떴냐')
stopwords.add('ㄹㅇ')


#여기서 만들어지는 이미지의 크기 및 폰트 등을 교체가능 합니다
wordcloud = WordCloud(font_path='font/Nanum.ttf', stopwords=stopwords, background_color='white', width=1000, height=1000, max_words=200, max_font_size=300).generate(text)

#이미지 생성
wordcloud.to_file('wordcloudman.png')

