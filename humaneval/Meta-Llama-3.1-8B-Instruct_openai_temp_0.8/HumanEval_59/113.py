```python
def largest_prime_factor(n: int):
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
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a loop to divide `n` by the smallest prime factor (starting from 2) until it can no longer do so. The remaining value of `n` will be the largest prime factor. The test cases demonstrate the function's correctness.