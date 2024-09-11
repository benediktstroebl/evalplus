```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): The number to be factorized
    
    Returns:
        List[int]: A list of prime factors
    """
    def is_prime(x: int) -> bool:
        """Check if a number is prime"""
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
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

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script first defines a helper function `is_prime(x)` that checks whether a given number `x` is prime. It then defines the `factorize(n)` function that finds the prime factors of a given number `n`. The function iterates from 2 to the square root of `n` to find factors, adding each factor to the list as it finds them. Finally, it checks whether `n` is greater than 1 and if so, adds it to the list as a factor. The function returns the list of factors.