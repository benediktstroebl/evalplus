```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # List all the numbers from 2 to sqrt(n) and check if it is divisible by any integer k with 1 <= sqrt(n)
    factors = [2] + [num for num in range(3, int(sqrt(n)) + 1) if n % num == 0]
    
    # Initialize a set to keep track of found factors
    factors_set = set()
    
    # Iterate over the numbers in the list
    for num in factors:
        if num not in factors_set:
            factors_set.add(num)
            times = n // num
            factors.append(factors_set.pop() if num in factors_set)
            factors.append(times)
    
    # Return list of prime factors
    return list(factors)
```