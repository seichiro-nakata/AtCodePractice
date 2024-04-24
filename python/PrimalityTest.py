# 入力値が素数であるかを判定する

import math

def isPrime(num):
  if num == 2:
    return True
  
  if num % 2 == 0:
    return False
  
  for i in range(3,int(math.sqrt(num)+1),2):
    if num % i == 0:
        return False
  
  return True

inputNum = int(input())

if(isPrime(inputNum)):
    print("Yes")
else:
    print("No")