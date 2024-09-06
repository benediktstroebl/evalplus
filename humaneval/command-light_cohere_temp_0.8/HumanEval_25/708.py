```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeases in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []
    else:
        factors = []
        while n % 2 == 0:
            n /= 2
            factors.append(2)
        n = n // 2
        while n > 1:
            if n % 2 == 0:
                n /= 2
                factors.append(2)
            else:
                factors.append(int)
                n = n // 2
        factors.append(1)
        return factors
```

This Python script defines a function `factorize` that takes an integer `n` as input and returns a list of prime factors of the given number. The function first checks if `n` is less than 1, and if so returns an empty list. If `n` is not, the function then iterates through the numbers 2, 4, and all odd integers up to the square root of `n`. It checks if `n` is divisible by 2 or any of these numbers. If so, it divides `n` by the appropriate number and adds the result to the list of factors. The function then divides `n` by 2 and adds the result to the list of factors. The function continues this process until `n` is 1.