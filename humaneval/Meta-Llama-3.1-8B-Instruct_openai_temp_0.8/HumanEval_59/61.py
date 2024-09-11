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

# Test the function
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2
```

This script works by dividing the input number `n` by increasing integers `i` until it finds a divisor. If `n` is divisible by `i`, it divides `n` by `i` and continues with the new `n`. If `n` is not divisible by `i`, it increments `i` by 1. The loop continues until `i` squared is greater than `n`. At this point, `n` is a prime number and is returned as the largest prime factor.