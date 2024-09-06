```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, )):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
def test_factorize(test_n: int) -> None:
    factors = factorize(test_n)
    for factor in factors:
        print(factor, end=' ')
    return factors == [2, 2, 2] * int(test_n ** 0.5)
```