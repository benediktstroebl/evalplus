```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors.
    """
    i = 2
    factors = []
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
if __name__ == "__main__":
    print(factorize(8))   # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

This script works by continuously dividing the input number `n` by the smallest prime factor until it is no longer divisible. The divisor (the prime factor) is then added to the list of factors. This process repeats until `n` is reduced to 1. If `n` is a prime number greater than 1, it is added as a single factor to the list.