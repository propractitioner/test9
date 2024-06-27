import streamlit as st
import random

# 일본 음식 리스트
japanese_foods = [
    "すし", "ラーメン", "とんかつ", "うどん", "そば",
    "sushi", "ramen", "tonkatsu", "udon", "soba",
    "お好み焼き", "牛丼", "天ぷら", "味噌汁", "たこ焼き",
    "okonomiyaki", "gyudon", "tempura", "miso soup", "takoyaki",
    "焼き鳥", "おにぎり", "カレーライス", "鍋", "牛カツ",
    "yakitori", "onigiri", "curry rice", "nabe", "gyukatsu"
]

def get_random_food():
    return random.choice(japanese_foods)

st.title("🍱 ランダムな日本のランチメニュー推薦")

st.write("日本料理が食べたいですか？ボタンを押してランダムな日本のメニューを推薦してもらいましょう！")

if st.button("日本のランチメニューを推薦する"):
    recommended_food = get_random_food()
    st.success(f"今日のお勧めの日本料理は「{recommended_food}」です！")
    st.balloons()

st.write("---")
st.write("メニューが気に入らない場合は、もう一度ボタンを押してください。")
