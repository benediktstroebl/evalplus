```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(101)
    []
    """
    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)

    for i in range(3, int(n ** 0.5),  #,):
        if n % i == 0:
            while n % (i * i) == 0:
                n //= i
            factors.append(i)

    return factors
```

This Python function, `factorize`, takes an integer `n` as input and returns a list of prime factors of the input number, ordered from smallest to largest. The function uses a `while` loop to find the prime factors of the number and stores them in the `factors` list. 

Please note that this function does not require any additional libraries and can be fully self-contained within the script.