import random

print("오징어 게임에 오신 것을 환영합니다.")
print("홀짝 게임을 시작합니다.")

#구슬 홀짝 게임의 규칙
#상대방이 구슬의 갯수를 정한다
#10개 이하의 무작위 수로 구슬의 갯수가 나왔으면 좋겠다
a=random.randint(1,10)
print(a)
#내가 홀 또는 짝을 얘기한다
#고정되어 있는 값을 사용자가 입력할 수 있으면 좋겠다 (1.홀 2.짝)

my = int(input("1.홀  2.짝 : "))
print(my)
if my == 1:
    print("1.홀")
else:
    print("2.짝")

#상대방 구슬의 갯수에서 2로 나누어서 나머지가 0이면 짝
#나머지가 1이면 홀
dab = ""
if a%2 == 0:
    print("짝")
    dab = 2
else:
    print("홀")
    dab = 1

#만약에 내가 얘기한 홀 또는 짝이 맞으면 맞았다
if my == dab:
    print("맞다")
#틀리면 틀렸다.
else:
    print("틀렸다. 빵!!!")
