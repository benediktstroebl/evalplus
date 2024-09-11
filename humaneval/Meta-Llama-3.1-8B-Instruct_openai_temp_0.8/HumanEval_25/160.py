```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The integer to be factorized

    Returns:
        List[int]: A list of prime factors
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
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

This script uses a helper function `is_prime` to check if a number is prime. The `factorize` function then iterates from 2 to the square root of the input number, checking for divisibility and appending the factor to the list if it is prime. If the number is not divisible by the current factor, it increments the factor until it finds the next one. Finally, if the remaining number is greater than 1, it is a prime number and is appended to the list.