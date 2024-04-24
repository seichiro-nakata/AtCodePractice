# 入力値以下の素数を小さい順に出力

def isPrime(num):
    if num < 2:
        return False
    
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

inputNum = int(input())

for i in range(2, inputNum + 1):
    if isPrime(i):
        print(i, end=' ')