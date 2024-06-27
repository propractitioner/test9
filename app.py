import streamlit as st
import random

# 일본 음식 리스트
japanese_foods = [
    "스시", "라멘", "돈카츠", "우동", "소바",
    "sushi", "ramen", "tonkatsu", "udon", "soba",
    "오코노미야키", "규동", "덴푸라", "미소시루", "타코야키",
    "okonomiyaki", "gyudon", "tempura", "miso soup", "takoyaki",
    "야키토리", "오니기리", "카레라이스", "나베", "규카츠",
    "yakitori", "onigiri", "curry rice", "nabe", "gyukatsu"
]

def get_random_food():
    return random.choice(japanese_foods)

st.title("🍱 무작위 일본 점심 메뉴 추천기")

st.write("일본 음식이 당기시나요? 버튼을 눌러 랜덤한 일본 메뉴를 추천받아보세요!")

if st.button("일본 점심 메뉴 추천받기"):
    recommended_food = get_random_food()
    st.success(f"오늘의 추천 일본 메뉴는 '{recommended_food}' 입니다!")
    st.balloons()

st.write("---")
st.write("메뉴가 마음에 들지 않으면 다시 버튼을 눌러보세요.")
