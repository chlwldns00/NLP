from textrank import KeywordSummarizer
import konlpy
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import scipy as sp

import pandas as pd

df=pd.read_csv("JEUS_application-client_final_DB(문단)_0705_new_eng.csv",encoding='utf-8',header=None)
df=df[3]
df=df[:10]  
df_list=df.values.tolist()
f=[]
for txt in df_list:
    txt=txt.replace('\n','')
    f.append(txt)
f='\n'.join(f)

#### 형태소 분석기
t=Okt()
def okt_tokenizer(sents):
#### data slicing(한글질문 위주, 100개만 잘라서 테스트)
    f[0]
    #print(len(contents))
    #print(df.head(3))



    #### 형태소 단위로 tokenize
    contents_tokens=[t.morphs(row) for row in sents]
    return contents_tokens

## textrank사용해서 키워드 추출 ##
keyword_extractor = KeywordSummarizer(
    tokenize = okt_tokenizer,    ## 수정해야할 파라미터 부분
    window = -1,
    verbose = False
)
keywords = keyword_extractor.summarize(f, topk=30)
for word, rank in keywords:
    print('{} ({:.3})'.format(word, rank))