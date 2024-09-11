Here is a self-contained Python script that solves the problem using the `sympy` library for prime number checking and list comprehension for factorizing the input number:

```markdown
### Prime Factorization Script
```python
from typing import List
import sympy

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
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

### Example Usage
if __name__ == "__main__":
    num1 = 8
    num2 = 25
    num3 = 70

    print(f"Prime factors of {num1}: {factorize(num1)}")
    print(f"Prime factors of {num2}: {factorize(num2)}")
    print(f"Prime factors of {num3}: {factorize(num3)}")
```

This script uses a simple trial division method to find the prime factors of the input number. It iteratively divides the number by the smallest prime factor (2), and for each division, it appends the divisor to the `factors` list. If the number is not divisible by the current prime factor, it increments the prime factor. The script continues this process until the number is reduced to 1, at which point it has found all prime factors. The `factorize` function returns the list of prime factors.

You can run this script in your Python environment to see the example usage and the prime factors of the given numbers.