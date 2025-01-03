import streamlit as st
import numpy as  np
import pandas as pd
from PIL import Image


st.title("試作版Webアプリ")

st.write("このWebアプリは試作版で内容に意味はありません。")

text=st.text_input("あなたの趣味を教えてください")
"あなたの趣味は",text


condition=st.slider("あなたの今の調子は？",0,100,50)
"あなたのコンディションは：",condition
if condition>60:
    st.write("GOOD!")
else:"頑張って！"
                 

#left_column, right_column = st.beta
#button=left_column.button("右カラムに文字を表示")
#if button:
#    right_column.write("ここは右カラムです")




df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.7],
    columns=["lat","lon"]
)
df
st.map(df)

st.write("Display Image")

if st.checkbox("写真を見る"):
    img= Image.open("gon.jpg")
    st.image(img,caption="以前飼っていた犬の写真です")

option=st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)
"あなたの好きな数字は",option,"です。"