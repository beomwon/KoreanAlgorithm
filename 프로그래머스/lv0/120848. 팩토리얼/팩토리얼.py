def solution(n):
    for i in range(1,12):
        num = 1
        for j in range(1,i+1):
            num*=j
        if num > n:
            return i-1  