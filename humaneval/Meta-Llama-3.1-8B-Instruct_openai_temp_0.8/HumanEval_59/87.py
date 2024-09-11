```python
def largest_prime_factor(n: int):
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

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script works by dividing the input number `n` by the smallest prime number `i` as long as `n` is divisible by `i`. The process is repeated until `n` is no longer divisible by `i`. At this point, `n` is a prime number, and it is the largest prime factor of the original number.