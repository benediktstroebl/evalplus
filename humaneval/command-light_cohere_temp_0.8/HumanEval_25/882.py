```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned in the order of their corresponding frequency in the factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    factors.append(int)
    n % 2 == 0
        factors.append(int)
    factors.append(n)
    return factors
```

The code provided defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors in the order of their corresponding frequency in the factorization. The function uses a while loop, starting with the assumption that `n` is even and then repeatedly divides `n` by 2 until it becomes odd. The function then adds the corresponding factors to the `factors` list.