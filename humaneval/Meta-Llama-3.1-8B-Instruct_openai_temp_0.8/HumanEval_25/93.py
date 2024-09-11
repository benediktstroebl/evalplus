### Prime Factorization Script
```markdown
### Description
This script provides a function `factorize` that takes an integer `n` and returns a list of its prime factors in the order from smallest to largest. Each factor is listed the number of times it appears in the factorization.

### Code
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
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

### Example Usage
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

### Explanation
The function `factorize` works by dividing the input number `n` by the smallest prime number (2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will be a prime number. This process continues until `n` is reduced to 1. The list of factors is built by appending each divisor to the list whenever `n` is divided by it.

Note that the function uses a while loop with a condition `i * i <= n` to improve efficiency, as it's unnecessary to check divisors greater than the square root of `n`. Also, the function handles the case when `n` itself is a prime number greater than 1.