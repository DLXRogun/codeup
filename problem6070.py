'''
월이 입력될 때, 계절 이름이 출력 되도록 해보자 

월 : 계절 이름
12, 1, 2 : winter
3, 4, 5 : spring
6, 7, 8 : summer
9, 10, 11 : fall


출처 : https://codeup.kr/problem.php?id=6070
'''
a = int(input())      # 사용자로부터 입력을 받고 정수형으로 변환

if a // 3 == 1 :      # a 를 3으로 나눈 몫이 1일 때.
    print("spring")   # spring 을 출력
elif a // 3 == 2:
    print("summer")
elif a // 3 == 3 :
    print("fall")
else:
    print("winter")

'''
이런 식으로 생각할 수 있구나
하나였던 길이 넓어져서 기록하기 위해 작성함. 

원래는

a == 12 or a == 1 or a == 2
이런식의 풀이를 하려고 함. 

근데 몫을 이용해서 하는 방법은 오,, 앞으로도 유용하게 쓸 거 같음.
'''