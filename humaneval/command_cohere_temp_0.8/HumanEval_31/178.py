Here's a Python script with a self-contained function `is_prime` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number `n` is prime or not. It first checks if `n` is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of `n` (inclusive), checking if `n` is divisible by any of these numbers, and if so, it returns `False`. If we reach the end of the loop, `n` is not divisible by any number up to its square root, and it's a prime number, so the function returns `True`.

This solution should help you pass any tests corresponding to the provided problem statement. Feel free to ask any further questions or request additional assistance.