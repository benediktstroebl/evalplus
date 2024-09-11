### Prime Factorization Script

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.
        """
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

# Example usage
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a recursive helper function `is_prime` to check for primality, and then uses a loop to find the prime factors of the input `n`. The loop iterates from 2 to the square root of `n`, and for each number `i` that divides `n`, it appends `i` to the `factors` list and divides `n` by `i`. If `n` is not divisible by any of the numbers in the range, it increments `i` by 1. The loop continues until `n` is reduced to 1, at which point any remaining prime factor `n` is appended to the `factors` list. The function returns the `factors` list.