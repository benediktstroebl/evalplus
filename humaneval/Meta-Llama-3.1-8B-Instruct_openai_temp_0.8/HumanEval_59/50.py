```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n (int): The number to find the largest prime factor of.
    
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

This script uses a while loop to find the largest prime factor of a given number `n`. It repeatedly divides `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. The process continues until `n` is a prime number, which is then returned as the largest prime factor.