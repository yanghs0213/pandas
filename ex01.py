import pandas as pd

print(pd.__version__)

# 판다스 : 데이터 입출력, 탐색, 정제, 변환, 집계, 분석... 편한게 메서드
# Series 클래스
# DataFrame 클래스

# pandas.py
# class Series: 1차원 배열 + 메서드
#    속성
#    메서드
# class Dataframe: 2차원 배열 + 메서드

s1 = pd.Series([1, 3, 5], index=[10, 20, 30]) # Series 클래스의 생성자(함수) 호출
print(type(s1))
print(s1)