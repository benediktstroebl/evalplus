```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of them is listed number of times, which corresponds to how many times they appear in factorization
    Input number should be equal to the product of all its factors.
    """
   
    prime factorization of 8 is [2, 2, 2]
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5, 2)):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for num in factors:
        if num > 1:
            factors.append(num)
        return factors
```
This function takes an integer n as input and returns a list of prime factors of n, in order from smallest to largest. It iterates through given number until all divisors are found, and then checks if each divisor divides the number evenly. The function then iterates through the possible prime divisors until the number itself is reached.