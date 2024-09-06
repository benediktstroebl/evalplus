Here's a Python script with a self-contained function that solves the prime-checking problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function checks if a given number `n` is prime or not. It first checks if `n` is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of `n` (inclusive), checking whether `n` is divisible by any integer in that range. If `n` is divisible by any of these integers, it returns `False`. However, if `n` isn't divisible by any integer in that range, it returns `True`, indicating that the number is prime. This approach is efficient due to the optimization of limiting the range of divisors to the square root of `n`.