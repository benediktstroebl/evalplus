```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in the order of their corresponding frequency in the factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    [7, 3, 3]
    >>> factorize(55)
    [5, 11]
    >>> factorize(1342)
    [2, 1342]
    >>> factorize(108)
    [2, 3, 54]
    """
    s = set(range(1, int(n**0.5) + 1))
    next(i for i in s if i <= int(n**0.5))
    next(i for i in s if i * i <= int(n**0.5))
    next(i for i in s if i * i > int(n**0.5))
    if n <= 1:
        return [n]
    else:
        # List of factors.
        factors = []
        for i in s:
            # Exclude the current number, i, as a factor.
            if i > int(n**0.5):
                continue
            for j in range(i, int(n**0.5) + 1):
                factors.append(j)
        return factors
``` 
The above Python code defines a function called `factorize` that aims to find the prime factors of a given integer `n`. It employs the set of numbers from 1 to `n` (inclusive) and uses the `next` function to iterate through these numbers. It then identifies the The numbers in the set that are less than or equal to `n` but greater than the square of `n` (i.e., numbers that can be factored out of `n`). Finally, it checks if `n` is less than or equal to 1 and, in such cases, returns `[n]` as the only prime factor. Otherwise, it constructs a list of all prime factors by iterating through the numbers in the set and excluding those already included in the list.