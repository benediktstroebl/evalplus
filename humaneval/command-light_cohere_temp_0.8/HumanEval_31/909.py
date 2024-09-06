Here is a self-contained Python function that checks whether a given number is prime:

```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

This code provides a function `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function uses a test several rules to determine primality, including the rule of 2 and 3, checking for divisibility by 6 numbers, and finally checking for divisibility by squares up to the number.