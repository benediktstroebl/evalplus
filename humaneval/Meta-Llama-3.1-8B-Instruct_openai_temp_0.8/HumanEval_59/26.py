```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    :param n: A positive integer greater than 1.
    :return: The largest prime factor of n.
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

This script uses a simple trial division method to find the largest prime factor of a given number. The algorithm works by dividing the input number `n` by increasing integers `i` until `i` is greater than the square root of `n`. If `n` is divisible by `i`, then `i` is a prime factor of `n` and `n` is divided by `i`. This process continues until `i` is greater than the square root of `n`. At this point, `n` is no longer divisible by `i` and `n` itself is the largest prime factor.