import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

largest = 0
product = 0

for a in range(-999, 999):
    for b in range(-1000, 1000):
      n = 0
      count = 0
      eqn = (n ** 2) + (a * n) + b
      while(is_prime(eqn)):
        count += 1
        n += 1
        eqn = (n ** 2) + (a * n) + b
      
      if count > largest:
         largest = count
         product = a * b
          

print(product)