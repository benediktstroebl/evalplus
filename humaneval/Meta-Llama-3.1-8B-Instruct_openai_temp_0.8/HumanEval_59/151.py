### Largest Prime Factor
#### Problem Solution in Python

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): The input number.

    Returns:
    int: The largest prime factor of n.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a given number `n`. It iteratively divides `n` by the smallest divisor `i` until `n` is reduced to its largest prime factor. This approach is more efficient than checking each number up to `n` for primality. The test cases at the end demonstrate the function's correctness.