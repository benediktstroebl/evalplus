### Factorize Function
```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize.

    Returns:
        List[int]: A list of prime factors of the input number.
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
    # Count occurrences of each factor
    factor_counts = {}
    for factor in factors:
        if factor in factor_counts:
            factor_counts[factor] += 1
        else:
            factor_counts[factor] = 1
    # Create final list with correct counts
    final_factors = []
    for factor, count in factor_counts.items():
        final_factors.extend([factor] * count)
    return final_factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a trial division method to find the prime factors of a given number. It starts by dividing the number by the smallest prime number, 2, and continues dividing by increasing integers until it finds a divisor. If the number is not divisible by the current integer, it increments the integer and continues the search. When a divisor is found, the number is divided by the divisor and the divisor is added to the list of factors. This process continues until the number is reduced to 1, at which point all its prime factors have been found. The final list of factors is then adjusted to include the correct counts for each factor.