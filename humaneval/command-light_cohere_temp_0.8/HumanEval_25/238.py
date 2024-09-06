```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization of the number.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    []
    """
    if n <= 1:
        return []

    # To maintain the order of factors, we will generate a list of numbers from 1 to n and
    # perform loop until sqrt(n) for each value.
    factors = [List[i=1, n] for i in range(1, n+1) do
        if n % i == 0:
            factors.append(i)
            factors.append(n // i*i)

    factors = factors[:-len(factors)//2]  # for optimal space

    # There should be only prime factors left.
    # If first factors with even a factor.
    # To check each of the factors in factors list to make sure it's prime.
    # If first factor is 2 (for n=8), which is prime.
    for i in range(len(factors)):
        if not factors[i]:
            break
    else:
        factors[i] = factors[0]  # if all factors are prime, then this is our answer

    return factors
```