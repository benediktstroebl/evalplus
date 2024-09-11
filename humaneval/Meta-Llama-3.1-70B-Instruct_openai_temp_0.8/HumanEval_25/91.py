```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize.

    Returns:
        List[int]: A list of prime factors in ascending order.
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for possible_factor in range(2, n + 1):
        # We only consider prime numbers as possible factors
        if is_prime(possible_factor):
            while n % possible_factor == 0 and n > 1:
                factors.append(possible_factor)
                n //= possible_factor
    return factors


# Example use cases
if __name__ == "__main__":
    print(factorize(8))  # Expected output: [2, 2, 2]
    print(factorize(25))  # Expected output: [5, 5]
    print(factorize(70))  # Expected output: [2, 5, 7]
```

This script works by checking each number up to the input number `n` to see if it is a prime factor. If it is, it keeps dividing `n` by this factor until `n` is no longer divisible by it. This process repeats until `n` is reduced to 1, at which point all its factors have been found. The `is_prime` helper function checks whether a number is prime.