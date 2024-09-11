```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n (int): A composite number greater than 1.
    
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
print(largest_prime_factor(13195))  # Expected output: 29
print(largest_prime_factor(2048))   # Expected output: 2
```

This script defines a function `largest_prime_factor` that finds the largest prime factor of a given number `n`. It does this by dividing `n` by the smallest prime number (2) as long as `n` is divisible by it, then by the next prime number (3), and so on, until `n` is reduced to its largest prime factor. The function returns this largest prime factor. The test cases at the end demonstrate the function's correctness.