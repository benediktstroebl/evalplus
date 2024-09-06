```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function iterates from 2 up to `n - 1` and checks if any number in this range divides the number `n`. If any such number is found, the function returns `False`, indicating that `n` is not prime. If no such number is found, the function returns `True`, indicating that `n` is prime.