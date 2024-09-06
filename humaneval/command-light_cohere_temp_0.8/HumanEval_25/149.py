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
    >>> factorize(1)
    []
    >>> factorize(13)
    [13]
    >>> factorize(10)
    Traceback (most recent call last):
      File "<stdin>", line 3, in <module>
        10
    ZeroDivisionError: division by zero
    """
    if n == 0:
        raise ZeroDivisionError("division by zero")
    prime = []
    for i in range(2, n + 1):
        if n % i == 0:
            while n % i == 0:
                n //=i
            prime.append(i)
    else:
            break
    return prime
```