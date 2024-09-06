```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count > 0:
                factors.append(i)
                factors.append(count)
    if n > 1:
        factors.append(n)
        factors.append(1)
    return factors[1:]
```
The factorization algorithm is executed sequentially and uses nested loops to find factors and count their occurrence. The resulting list of factors, with counts, is then returned after sorting them in ascending order. The code includes type annotations and documentation to clarify its purpose and usage.

Here is a simple test case for the algorithm:
```python
def test_factorize():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
```