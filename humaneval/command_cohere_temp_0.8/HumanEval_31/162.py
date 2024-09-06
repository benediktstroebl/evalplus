```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function rigorously checks whether `n` is prime by iterating through a range of integers from 2 up to the square root of `n` (inclusive). If `n` is divisible by any of these integers, it's not a prime number, and the function returns False. If `n` isn't divisible by any of them, it's a prime number, and the function returns True. This ensures an accurate assessment of primality for integers inputted to the function.