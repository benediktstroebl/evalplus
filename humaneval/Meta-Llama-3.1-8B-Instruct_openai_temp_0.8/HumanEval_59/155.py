```python
def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    max_factor = 1
    for i in range(2, n + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # Check if i is prime
            if is_prime(i):
                max_factor = max(max_factor, i)
    return max_factor


# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `is_prime` to check if a number is prime, and a function `largest_prime_factor` to find the largest prime factor of a number. The `largest_prime_factor` function iterates from 2 to `n` and checks if each number is a factor of `n` and prime. The largest prime factor is returned at the end of the script. 

However, this script has a time complexity of O(n^2) due to the nested loop in the `largest_prime_factor` function. A more efficient solution can be achieved by iterating up to the square root of `n` and dividing `n` by each factor. 

Here's a more efficient version of the script:

```python
import math

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    max_factor = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0 and is_prime(i):
            max_factor = max(max_factor, i)
            n //= i
    if n > 1 and is_prime(n):
        max_factor = max(max_factor, n)
    return max_factor


# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This version of the script has a time complexity of O(sqrt(n)) due to the iteration up to the square root of `n`.