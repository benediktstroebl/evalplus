```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize

    Returns:
        List[int]: A list of prime factors
    """
    def is_prime(x: int) -> bool:
        """Check if number is prime"""
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

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script first defines a helper function `is_prime` to check if a number is prime. Then, it uses a while loop to find the prime factors of the input number `n`. If `n` is divisible by `i`, it divides `n` by `i` and adds `i` to the list of factors. It continues this process until `n` is no longer divisible by any number up to its square root. If `n` is a prime number greater than 1, it adds `n` to the list of factors. Finally, it returns the list of factors.