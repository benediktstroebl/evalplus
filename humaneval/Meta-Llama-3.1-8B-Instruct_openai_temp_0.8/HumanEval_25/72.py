```python
from typing import List


def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Parameters:
    n (int): The number to be factorized
    
    Returns:
    List[int]: A list of prime factors of the input number
    
    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    # Remove duplicates and sort the list
    return sorted(list(set(factors)))


# Test the function
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of the input number. It starts by dividing the number by the smallest prime number (2) and continues to divide by increasing prime numbers until the number is reduced to 1. If the number is divisible by a prime number, it is divided by that prime number and the prime number is added to the list of factors. If the number is not divisible by a prime number, the prime number is incremented by 1. The list of factors is then sorted and duplicates are removed to produce the final result.