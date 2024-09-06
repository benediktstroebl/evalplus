```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(9)
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
        9
    ValueError: invalid literal for int() with base 10: '9'
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    if n <= 1:
        break
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        n /= i
        factors.append(i)
    if n <= 1:
        break
    return factors
```