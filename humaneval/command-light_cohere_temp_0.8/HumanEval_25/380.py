```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors
    """
    factors = []
    for i in range(1, int(n**0.5)+1):
        while n % i == 0:
        factors.append(i)
        n //= i
    factors.append(n)
    return factors
```

This function uses a loop to find all the prime factors of the given number and stores them in a list. It returns the list of prime factors in the order of their appearance in the factorization of the original number.