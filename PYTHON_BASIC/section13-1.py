# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

# 영어 단어 리스트(1000개 로드)
words = []
# 게임 시도 횟수
n = 1
# 정답 개수
cor_cnt = 0

with open('./resource/word.txt', 'r') as f :
    for c in f :
        # 양쪽 공백 제거
        words.append(c.strip())

# 단어 리스트 확인        
# print(words)

input("Ready? Press Enter Key!")

# 시작 시간 기록
start = time.time()

while n <= 5 :
    random.shuffle(words)
    # 랜덤으로 하나 선택
    q = random.choice(words)

    print()

    print("Question #{}".format(n))
    # 문제 출력
    print(q)
    # 타이핑 입력
    x = input()
    print()

    # 입력 확인(공백 제거)
    if str(q).strip() == str(x).strip() :
        print('Pass!')
        cor_cnt += 1
    else :
        print('Wrong!')
    
    n += 1

end = time.time()
# 총 게임 시간
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3 :
    print('합격')
else :
    print('불합격')

# 수행시간 출력
print('게임 시간 :', et, '초')
print('정답 개수 : {}'.format(cor_cnt))

# 시작 지점
if __name__ == "__main__" :
    pass