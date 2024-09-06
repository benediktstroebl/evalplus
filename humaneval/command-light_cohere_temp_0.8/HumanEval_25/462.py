```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in the order of their corresponding rank in the factorization.

    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(76)
    [2, 2, 2, 7]
    >>> factorize(1)
    Traceback (most recent call last):
      File "<stdin>", line 7: ...
    TypeError: 'int' object does not support item assignment and fewer than 8 bytes long
    """
    if n <= 0:
        raise ValueError("The given number should be a positive integer.")

    # Step 1: Determine the maximum power of each prime number less than or equal to the square root of n.
    # Iterate through prime numbers until the maximum power of a prime number is less than or equal to the square root of the number, and there is a finite set of such prime numbers.
    mps = []
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            mps.append(num)
            mps.append(n //
        if n % (num * num) == 0:
                mps.append(num * num)
                mps.append(1)
    if n % (num * 2) == 0:
                mps.append(num * 2)
                mps.append(num)
                mps.append(1)

    # Step 2: Determine the factors of n by multiplying each of the prime factors.
    factors = []
    for p in mps:
        factors.append(p * n // n)
        factors.append(factors[-1] / factors[-2])

    # Return the list of prime factors in the order from smallest to largest.
    return factors
 return factors
```