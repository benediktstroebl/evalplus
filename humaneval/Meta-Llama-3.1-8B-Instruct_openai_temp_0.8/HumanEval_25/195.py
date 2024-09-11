### Prime Factorization
#### Python Script
```markdown
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
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
        """Check if a number is prime."""
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

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
    return factors

# Example use cases
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```
This Python script defines a function `factorize` to calculate the prime factors of a given integer. The function uses a helper function `is_prime` to check if a number is prime. The main function iterates over numbers from 2 to the square root of the input number, and for each number, it checks if it is a factor of the input number. If it is, the number is repeatedly divided by the factor until it is no longer divisible. The resulting list of factors is returned.