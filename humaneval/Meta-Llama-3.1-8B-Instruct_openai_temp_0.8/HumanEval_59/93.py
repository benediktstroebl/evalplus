```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n (int): The number to find the largest prime factor of.
    
    Returns:
    int: The largest prime factor of n.
    
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
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

This script uses a while loop to divide the input number `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. It increments `i` by 1 in each iteration. When `n` is no longer divisible by `i`, it means `i` is the largest prime factor of `n` that is smaller than the square root of `n`. The loop continues until `i * i` is greater than `n`. Then, `n` is the largest prime factor of the original number.