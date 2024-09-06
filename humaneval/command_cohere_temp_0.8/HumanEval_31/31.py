```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement and test scenarios provided, correctly identifying prime and non-prime numbers. It iterates through numbers from 2 up to the square root of the input number, checking for divisibility. If the number is divisible by any factor within this range, it's not prime, and the function returns `False`. If not, it's prime, and the function returns `True`. This approach is efficient due to the optimized range of iteration.

However, it's worth mentioning that the current script doesn't match the provided docstring. The function has been rewritten as it was not clear enough in the initial version.