Here's a Python script that uses a function called `factorize` which takes an integer `n` as input and returns a list of prime factors. This script uses a helper function to check if a number is prime.

```markdown
### Prime Factorization Script

#### Problem Description

This script calculates the prime factorization of a given integer.

#### Code

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

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

#### Explanation

The `is_prime` function checks if a given number `n` is prime. It first handles the edge cases where `n` is less than or equal to 1, and then checks if `n` is divisible by 2. If it is not, the function checks divisibility by all odd numbers up to the square root of `n`.

The `factorize` function calculates the prime factorization of a given integer `n`. It starts by initializing an empty list `factors` to store the prime factors. It then enters a loop that continues until the square of the loop counter `i` is greater than `n`. Inside the loop, it checks if `n` is divisible by `i`. If it is not, it increments `i` by 1. If it is, it divides `n` by `i` and appends `i` to the `factors` list. After the loop ends, it checks if `n` is greater than 1. If it is, it appends `n` to the `factors` list. Finally, it returns the `factors` list.

#### Example Use Cases

You can use the `factorize` function to calculate the prime factorization of any integer. For example, you can use the following code to calculate the prime factorization of 100:

```python
print(factorize(100))  # [2, 2, 5, 5]
```