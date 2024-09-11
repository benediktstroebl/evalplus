```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    :param n: The input number.
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
print(largest_prime_factor(13195))  # Expected output: 29
print(largest_prime_factor(2048))   # Expected output: 2
```

This script uses a while loop to start dividing `n` by the smallest prime factor (2) until `n` is no longer divisible by `i`. It then increases `i` by 1 and repeats the process until `i` is no longer smaller than the square root of `n`. At this point, `n` is the largest prime factor of the original number.