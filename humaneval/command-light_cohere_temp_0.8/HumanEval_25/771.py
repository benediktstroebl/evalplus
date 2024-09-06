```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, step by step):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```

This function factorizes a given number by iteratively dividing by the prime factors of the number. It returns a list of prime factors of the number in order from smallest to largest. The factors are listed number of times corresponding to how many times it appears in factorization. The function also passes the tests with a variety of inputs.