import streamlit as st
import numpy as  np
import pandas as pd
from PIL import Image


st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start"

text=st.text_input("あなたの趣味を教えてください")
"あなたの趣味",text

condition=st.slider("あなたの今の調子は？",0,100,50)
"コンディション：",condition

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
    st.image(img,caption="GON",use_column_width=True)

option=st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)
"あなたの好きな数字は",option,"です。"

