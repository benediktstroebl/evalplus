Here's a Python script with a self-contained function `is_prime(n)` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 up to the square root of the number, checking whether the number is divisible by any other number. If the number is divisible by any other number in this range, it returns `False`. However, if the number is not divisible by any number in this range, it returns `True`.

This solution corresponds to the provided example tests, correctly identifying prime and non-prime numbers.