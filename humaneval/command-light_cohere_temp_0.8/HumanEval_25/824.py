```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        for i in range(3, int(n**.5) + 1, by=2):
            if n % i == 0:
                factors.append(i)
                n = n // i
    return factors
# Test the function
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This function, `factorize`, accepts an integer `n` as input and returns a list of its prime factors. The function employs a technique of dividing by primes to find the prime factors, checking for divisibility by each prime number up to the square root of `n`. The function works by starting with the smallest prime number (2) and gradually increases the prime until it reaches the square root of `n`.