### Factorize Function
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
        List[int]: A list of prime factors of the input number.

    Examples:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """

    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
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

    # Count the occurrences of each factor
    factor_counts = {}
    for factor in factors:
        if factor in factor_counts:
            factor_counts[factor] += 1
        else:
            factor_counts[factor] = 1

    # Construct the final list of factors
    result = []
    for factor, count in factor_counts.items():
        result.extend([factor] * count)

    return result

# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a `factorize` function that takes an integer `n` as input and returns a list of its prime factors. The function uses a helper function `is_prime` to check if a number is prime. It then iterates through the numbers from 2 to the square root of `n` to find the prime factors. If `n` is divisible by a number, it is divided by that number and the number is added to the list of factors. If `n` is not divisible by any number, it is itself a prime number and is added to the list of factors. The function then counts the occurrences of each factor and constructs the final list of factors.

The script also includes example usage of the `factorize` function to demonstrate its correctness.