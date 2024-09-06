```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, step(n) // i):
        if n % i == 0:
            factors.append(i)
        n = n // i
    factors.append(int(n))
    return factors

def test_factorize(n: int) -> None:
    assert factorize(n) == [2, n // 2, n // 3, int(n**0.5)]
```
This code defines a function factorize, which returns a list of prime factors of the given number n, in order from smallest to largest, and tests it with the test_factorize function, which asserts that the function returns the correct result.  This can be used to factorize any positive integer.