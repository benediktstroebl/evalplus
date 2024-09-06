```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, ]:
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(int(n**0.5) + 2,  - 1):
        if n % j == 0:
            factors.append(j)
    return factors
```
The provided Python script defines a function factorize that calculates and returns a list of prime factors for a given integer n. It starts by checking if n is less than or equal to 1, in which case it returns an empty list. Then, it enters a loop that continuously divides n by the smallest prime factor (starting from 2) until n is divisible by at least one of these factors. The while loop effectively identifies and appends each prime factor to the factors list. The script also includes a nested loop that iterates through the prime factors (from 3 up to the square root of n) while checking for divisibility. Finally, it appends the smallest prime factor j to the list if n is not a prime number and returns the list of prime factors in ascending order.