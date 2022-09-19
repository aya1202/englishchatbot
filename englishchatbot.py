import streamlit as st
import numpy as np
import pandas as pd

st.title("英語質問アプリ")
st.subheader("英語学習の質問に答えるテストアプリです")

st.text("全国から寄せられたお問い合わせを元に、英語学習の質問にAIが答えます。\n今は精度が高くありませんが、データが増えるにつれて\nよりよい回答をご提示できるように成長予定。\nネコの手も借りたい時の相棒としてお使いください😺")

#テキストボックス（入力ウィンドウ）🐈
question = st.text_input("質問を入力🐈")
print(question)

#ボタン
submit_btn = st.button("質問する")
cancel_btn =st.button ("やり直す")
print(f"submit_btn: {submit_btn}")
print(f"cancel_btn: {cancel_btn}")

#st.text("疑問は解消しましたか？")
#yes_btn = st.button("はい")
#no_btn = st.button("いいえ")
