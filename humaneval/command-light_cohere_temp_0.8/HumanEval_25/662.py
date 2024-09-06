```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    if not n: return []
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
    n = n // 2
    for i in range(3, int(n**0.5) // + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
The function factorize takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The function first checks if n is even and returns an empty list if n is 0. Then, it enters a while loop and keeps dividing n by the smallest prime number until n is divisible by the current prime number. The prime number is added to the list of factors with the corresponding number of times n is divisible by the prime number. The loop continues until the smallest prime divisor of n is found.