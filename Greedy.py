'''
현재 상황에서 지금 당장 좋은것만 고르는 방법
일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
정당성 분석이 중요 - 가장 좋아보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토
'''

'''
예시 ) 루트노드부터 시작하여 거쳐가는 노드 값의 합을 최대로 만들고 싶습니다.
Q. 최적의 해는 무엇인가요?
5-7-9 = 21
                        5
               7       10          8
        7   5   9     4  3       1   4   5                  
Q. 단순히 가장 큰 값만 고른다면 5-10-4=19
'''
'''
탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 풀리도록 제출
대표적인 예시 ) 거스름 돈 문제
- 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문
'''
# 거스름 돈 답안
from re import I
from turtle import numinput


n = 1260    # 거스름 돈
count = 0

array = [500,100,50,10]

for coin in array :
    count += n // coin      # 해당 화페로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 시간 복잡도
'''
화폐의 종류가 K라고 할 때, 소스코드의 시간 복잡도는 O(K)
거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받음
'''
  
'''
C++

#include <bits/stdc++.h>
using namespace std;

int n = 1260;
int cnt;

int cointype[4] = {500,100,50,10};

int main(void) {
    for (int i=0; i<4; i++){
        cont += n/cointype[i];
        n %= cointype[i];
    }
    count << cnt << '\n';
}
'''

'''
문제 : 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
1. N에서 1을 뺍니다.
2. N을 K로 나눕니다.   (단, N이 K의 배수일 경우만 가능)
N과 K가 주어질 때 N이 1이 될 때까지 1번or2번의 과정을 수행해야하는 최소 횟수를 구하시오
'''
'''
정당성 분석)
가능하면 최대한 많이 나누는 작업이 최적의 해를 항상 보장할 수 있을까?
'''
'''
# 대헌 구현
N, K = map(int, input().split())
count =0

while True :
    if N % K == 0 :
        N / K
        count += 1
    elif N == 1:
        break
    else :
        N -= -1
        count += 1
print(count)
'''
#정답
n,k = map(int,input().split())
result = 0

while True :
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k             # target에 대입 = n을 k로 나눈 몫*k 
                                    # N이 k로 나누어 떨어지지않더라고 해도 K로 떨어지는 가장 가까운 N값을 찾을 수 있음
    result +=(n-target)             # 1을 몇번 빼야되는지 계산
    n = target
    # N이 K보다 적을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

'''
문제 : 각 자리가 숫자(0부터9)로만 이루어진 문자열 S가 주어질때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를
확인하여 숫자 사이에 'x'혹은 '+' 연산자를 넣어 결과적으로 만들어 질 수 있는 가장 큰 수를 구하는 프로그램
을 작성하시오
단, +보다 x를 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽부터 이루어진다고 가정
만들어지는 수의 가장 큰값은 항상 20억 이하의 정수
'''
'''
 # 대헌 구현

S = list(input())

result = 1

print(S)
for i in S :
    if int(i) <= 1 :
        result += int(i)
    else :
        result *= int(i)

print(result)
# input 이 0이 들어와도 결과값이 1이 나오기때문에, result 초기화시 1 Nope
# result에 처음 input값 넣는게 나음

# 해설
'''
# 0 혹은 1일 경우는 더하기를 수행 / 이외는 곱하기 수행
'''
data = input()
# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)) :
    # 두 수 중 하나라도 0 혹은 1인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else :
        result *= num

print(result)
'''

'''
문제 ) 한 마을에 모험가 N명이 있음 / 각 모험가마다 공포도가 있음
공포도가 X인 모험가는 반드시 X명 이상으로 구성된 모험가 그룹에 참여해야만 여행을 떠날 수 있음
N명의 모험가에 대한 정보가 주어졌을 때 최대 몇 개의 모험가 그룹을 만들 수 있는가? 
'''
'''
예시) N = 5 이고, 공포도는 2 3 1 2 2 와 같다
첫번째 줄에 N이 주어지며,
둘째 줄에는 각 모험가의 공포도가 N이하의 자연수로 공백을 기준으로 주어진다
'''

# 대헌
N = int(input())
fear = list(map(int,input().split()))
fear = sorted(fear)



# 해설
# 오름차순 정렬하여, 앞에서부터 공포도를 하나씩 확인하여
# '현재 그룹에 포함된 모험가의 수'가 현재 확인하고 있는 공포도보다 크거나 같다면, 이를 그룹으로 설정

n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0      # 총 그룹의 수
count = 0       # 현재 그룹에 포함된 모험가의 수

for i in data :         # 공포도를 낮은 것 부터 하나씩 확인
    count += 1          # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:      # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹 결성
        result += 1     # 그룹 수 증가
        count = 0       # 모험가 수 초기화

print(result)
















