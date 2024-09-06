Here's a Python script with a self-contained function `is_prime(n)` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number `n` is prime or not. It first checks if `n` is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of `n` (inclusive), checking whether `n` is divisible by any of these numbers. If `n` is divisible by any of them, it returns `False`. However, if it isn't, it returns `True`, indicating that the number is prime. 

This implementation provides an efficient algorithm for checking primality, making it suitable for a wide range of applications involving prime number verification.