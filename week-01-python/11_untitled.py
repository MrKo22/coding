# 과제_1_맛집고르기
import random
menu = input("한식, 중식, 일식 중 하나를 골라주세요!")

한식 = ["김치찌개", "순대국", "감자탕"]
중식 = ["짜장면", "짬뽕", "탕수육"]
일식 = ["스시", "돈까츠", "오꼬노미야끼"]

if menu == "한식":
    print(random.choice(한식))

elif menu == "중식":
    print(random.choice(중식))

elif menu == "일식":
    print(random.choice(일식))

else:
    print("한식, 일식, 중식 중에 한가지만 선택!")

#result = ""
#if menu == "한식":
#    result = random.choice(한식)
#elif menu == "중식":
#    result = random.choice(중식)
#elif menu == "일식":
#    result = random.choice(일식)
#else:
#    print("한식, 일식, 중식 중에 한가지만 선택!")
#
#print(result)
