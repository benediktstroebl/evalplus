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

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning `False` if so. Then, it iterates from 2 up to the square root of the number, checking whether the number is divisible by any integer in this range. If the number is divisible by any of these integers, it returns `False`. If it is not divisible by any of them, it returns `True`.

This algorithm is more efficient compared to checking all integers up to `n` since it eliminates a lot of candidates for divisors during the process.