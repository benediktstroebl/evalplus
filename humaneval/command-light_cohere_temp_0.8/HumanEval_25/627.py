```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
def test_factorize(test_n: int) -> None:
    assert factorize(test_n) == [2, 2, 2]  # [2, 2, 2] should be the prime factors of 8
    assert factorize(25) == [5, 5]  # [5, 5] should be the prime factors of 25
assert factorize(70) == [2, 5, 7]  # [2, 5, 7] should be the prime factors of 70
```