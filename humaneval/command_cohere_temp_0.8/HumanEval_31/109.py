```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function rigorously checks whether `n` is divisible by any number from 2 to the square root of `n`, returning `False` if it is and `True` otherwise. This is sufficient to determine primality for all positive integers.