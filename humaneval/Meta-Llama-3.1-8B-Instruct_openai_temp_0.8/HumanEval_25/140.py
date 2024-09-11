### Prime Factorization Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The input number to be factorized.

    Returns:
    List[int]: A list of prime factors.

    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """

    def is_prime(x: int) -> bool:
        """ Helper function to check if a number is prime """
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    factors = []
    i = 2
    while n > 1:
        if n % i == 0 and is_prime(i):
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors.extend([i] * count)
        i += 1

    return factors
```

### Example Usage
```python
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```