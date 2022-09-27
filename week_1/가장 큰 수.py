# 정렬 - 가장 큰 수
def solution(numbers):
    answer=[]
    numbers=[str(x) for x in numbers]
    numbers.sort(key=lambda x:(x*4)[:4],reverse=True)
    if numbers[0]=='0':
        answer='0'
    else :
        answer=''.join(numbers)
    return answer

# 다른 사람의 풀이
'''
def solution(numbers):
    answer=[]
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num*3, reverse=True)
    print(numbers_str)
    answer=int(''.join(numbers_str))
    return str(answer)
'''
# 입력이 [0,0,0] 이면 결과로 0이 나와야한다.
# print('문자열0을 상수로 변환',int('000')) 출력해보면
# 0이 나옴을 알 수 있다.

# 나의 풀이(모든 조합을 구하기 때문에 효율성 꽝)
'''
from itertools import permutations
def solution(numbers):
    answer=[]
    comb=[]
    comb=map(list,permutations(numbers,len(numbers)))

    for i in comb:
        answer.append(''.join(str(x) for x in i))
    answer=(map(int,answer))
    return max(answer)
'''