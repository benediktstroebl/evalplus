```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function rigorously checks whether a given number `n` is divisible by any number from 2 to the square root of `n`, if not, it is deemed prime. This approach ensures accuracy and computes prime checks for large numbers efficiently. Enjoy conducting further prime investigations with this foundational function!