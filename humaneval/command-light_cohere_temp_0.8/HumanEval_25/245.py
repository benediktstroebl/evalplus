```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    ```
    algorithm:
    - Initialize a set of primes and 0
    - Iterate from 2 to the square root of n while adding the square of each number to the primes set, if it is prime.
    - If numbers greater than the square root of n will be added to the product
    - Repeat the above step, until the square of all numbers are added to the product
    - At this point, the product will be a prime number
    - Extract factors from the product from the above step by dividing it by primes until the quotient is not equal to zero
    - The numbers obtained during the quotient are the prime factors
    """
    factors: List[int] = []
    while n > 1:
        if n % 2 == 0 or n % 3 == 0:
            factors.append(n)
        n // 2 or 3 = 0
        n = n // 2
    while n >= 2:
        if n % 2 == 0:
            factors.append(n) = n // 2
        n = n // 2
    for factor in factors:
        if factor > 1:
            print(f'{factor} is a prime factor')
        else:
            print(f'{factor} is not a prime')
    return factors
```