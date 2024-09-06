```python
from typing import List
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1,  while n % i == 0:
        factors.append(i)
        n = n // i
    for num in range(int(n**0.5)+1,  while n % num == 0 and num != 1:
        factors.append(num)
    return factors
``` 
This function, factorize, calculates the prime factors of a given number. It first checks for the prime factors of a given number, by checking divisibility of the number with all numbers starting from 3 up to the square root of the number, while keeping track of all factors found. It also makes sure that the list only contains prime numbers and is ordered from the smallest to the largest.