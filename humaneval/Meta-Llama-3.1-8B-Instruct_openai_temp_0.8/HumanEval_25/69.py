### Prime Factorization of an Integer

This script defines a function `factorize` that takes an integer as input and returns a list of its prime factors. The prime factors are listed in the order from smallest to largest, and each factor appears in the list as many times as it appears in the factorization of the input number.

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Parameters:
    n (int): The input number.

    Returns:
    List[int]: A list of prime factors of the input number.

    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """

    factors = []
    divisor = 2

    # Divide the input number by the divisor as long as it is divisible
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1

    return factors

# Example usage:
print(factorize(8))    # Output: [2, 2, 2]
print(factorize(25))   # Output: [5, 5]
print(factorize(70))   # Output: [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to divide the input number by the smallest prime number (2) as long as it is divisible, and then increments the divisor by 1. This process continues until the input number is reduced to 1. The list of prime factors is returned at the end of the function.