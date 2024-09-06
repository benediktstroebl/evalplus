```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all factors
    """
    if n < 2: return []
    factors = []
    while n % 2 == 0: factors.append(2)
    n = n // 2
    while len(factors) > 0 and n % factors[-1] == 0: factors.append(factors[-1])
        n = n // factors[-1]
    factors.append(factors[-1])
    return factors
```
This function takes an integer `n` as input and returns a list of prime factors of the number, ordered from smallest to largest. It starts by checking if `n` is divisible by 2. If so, it appends 2 to the `factors` list. Then, it continues by factoring `n` by dividing `n` by the largest factor that divides `n` evenly. The process continues until there are no more divisors or `n` becomes a prime number.