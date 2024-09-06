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

This function iterates through numbers from 2 up to the square root of the input number `n`, checking for divisibility. If the number is divisible by any integer within this range, it returns `False`, indicating that the number is not prime. However, if the number is not divisible by any integer within this range, it returns `True`, indicating that the number is prime.

This algorithm is efficient as it only needs to check up to the square root of `n`. Examples are provided to demonstrate the behavior of the function.