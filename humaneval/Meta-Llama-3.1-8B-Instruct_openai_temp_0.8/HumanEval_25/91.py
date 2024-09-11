### Factorize Integer into Prime Factors
#### Python Script

```markdown
from typing import List
import math


def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Integer to be factorized

    Returns:
        List[int]: List of prime factors

    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            # Find the highest power of the current factor
            power = 0
            while n % (i ** (power + 1)) == 0:
                power += 1
            factors.extend([i] * power)  # Extend the list with the factor repeated power times
            n //= i ** power  # Divide n by the factor
        else:
            i += 1
    return factors


# Example usage
if __name__ == "__main__":
    print(factorize(8))   # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a loop to check for divisibility from 2 to the square root of `n`. When a divisor is found, it calculates the highest power of the divisor that divides `n`, adds the corresponding number of instances of the divisor to the `factors` list, and divides `n` by the divisor raised to that power. The loop repeats until `n` is reduced to 1. The script then returns the list of prime factors.