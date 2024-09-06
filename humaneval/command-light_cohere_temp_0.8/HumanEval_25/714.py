```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the same number of times corresponding to the original value.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(77)
    [3, 3, 7]
    >>> factorize(106)
    [2, 3, 5, 7]
    >>> factorize(9000)
    [3, 3, 2, 2, 2, 2, 2]
    """
    # Set of numbers that are equal to n or are divisible by n
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        s |= set([x for x in range(i, int(n ** 0.5) if n % x == 0])
        # Set of numbers divisible by n that are not equal to n
        v = set()
        for x in s:
            v |= set([i for i in range(x, int(n ** 0.5) if n % i == 0])
        # Create list of prime numbers that are divisible by n but not equal to n
        p = [x for x in v if x not in s]
        # Sort the list of prime numbers
        p.sort()
        # - last prime number in the list is n
        return p
    ```