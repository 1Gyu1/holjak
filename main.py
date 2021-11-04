print("오징어 게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다")

# 구슬로 홀짝 게임 규칙
# 상대방이 구슬의 갯수를 정한다
import random
a = 5  # 10개 이하의 무작위 수로 구슬의 갯수가 나왔으면 좋겠다.
a = random.randint(1, 10)
################print(a)
# 내가 홀 또는 짝을 얘기한다
my = "짝"  # 고정되어 있는 값을 사용자(내)가 입력을 받을 수 있었으면 좋겠다.(1.홀, 2.짝)

# 참가자가 가진 구슬의 갯수
marble = 10

#구슬의 갯수를 알려주자
print("당신의 구슬의 갯수 : {}개".format(marble))  #print("당신의 구슬의 갯수 : ".marble)

#  한번은 반복을 했으면 좋겠다
while 1:
    
    
    #구슬의 갯수 배팅
    try:
        bet = int(input("구슬 몇개 배팅? : "))
        if marble < bet:
            print("당신의 구슬이 부족하다 다시 배팅하시오")
            continue
    except:
        print("숫자만 입력하세요")
        continue

    my = input("홀 짝? (잘 못쓰면 빵이지만 한번은 기회줄게) : ")
    #################print(my)
    # 만약에 홀, 짝이 아니면 잘못입력 메세지
    if my == "홀" or my == "짝":
        # 상대방의 구슬의 갯수에서 2로 나누어서 나머지가 0이면 짝
        # 나머지가 1이면 홀
        dab = ""
        if a % 2 == 0:
            print("짝")
            dab = "짝"
        else:
            print("홀")
            dab = "홀"

        # 만약에 내가 얘기한 홀 과 짝 중에 맞으면 맞다
        if my == dab:
            print("맞다")
            marble += bet
            print("당신의 구슬의 갯수 : {}개".format(marble))
        # 틀리면 틀렸다
        else:
            print("아 졌다... 뺏겼네..")
            marble -= bet
            print("당신의 구슬의 갯수 : {}개".format(marble))

        #만약에 구슬의 갯수가 0이하면 게임종료
        if marble <= 0:
            print("당신은 게임에서 졌습니다")
            break
        #만약에 구슬의 갯수가 20이상이면 게임승리
        elif marble >=20:
            print("당신은 게임에서 승리했습니다")
            break

    else:
        print("잘못 입력 다시 입력해라")
