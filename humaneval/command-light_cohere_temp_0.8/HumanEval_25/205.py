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
    factors.append(n)
    return factors
def test_factorize():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
```
The code defines a function `factorize` that returns a list of prime factors of a given number `n`. The function first handles the case where `n` is even by appending `2` to the list of factors. Then, for numbers starting from 3 up to the square root of `n`, the function checks if `n` is divisible by `i`. It then divides `n` by `i` and appends the `i` to the list of factors. The function then returns the factorization as a list of numbers, where each number appears the number of times it appears in the factorization.