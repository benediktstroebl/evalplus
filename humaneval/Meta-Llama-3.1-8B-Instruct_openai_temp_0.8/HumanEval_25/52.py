### Prime Factorization Script

Below is a Python script that uses a helper function to check for primality and the main `factorize` function to find the prime factors of a given number.

```markdown
### Code
```python
from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
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
    return factors

# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

### Explanation

*   The `is_prime` function checks if a number is prime by dividing it by all numbers up to its square root.
*   The `factorize` function finds the prime factors of a number by dividing it by increasing integers until it finds a divisor.
*   Once a divisor is found, it is added to the `factors` list, and the number is divided by the divisor. This process repeats until the number is reduced to 1.
*   The `factorize` function returns the list of prime factors.
*   In the example usage section, the `factorize` function is called with three different numbers, and the output is printed to the console.