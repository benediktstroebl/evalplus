Here's a Python script that uses a helper function to check for primality, then finds the prime factors of a given integer.

```markdown
### Prime Factorization Script
#### Usage
This script takes an integer as input and returns its prime factors.

#### Code
```python
from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
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
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

#### Explanation
This script first defines a helper function `is_prime` to check if a number is prime. It then defines the `factorize` function, which takes an integer as input and returns its prime factors.
The `factorize` function works by iterating from the smallest prime number (2) up to the square root of the input number. For each number `i` in this range, it checks if `n` is divisible by `i`. If it is, it divides `n` by `i` and adds `i` to the list of factors. If `n` is not divisible by `i`, it increments `i` by 1 and repeats the process. The process continues until `n` is reduced to 1, at which point the function returns the list of factors.
Finally, the script includes some test cases to verify that the `factorize` function works correctly.