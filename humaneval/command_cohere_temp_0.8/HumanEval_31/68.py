Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
The function `is_prime` takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function first checks if `n` is less than 2, returning `False` if so. It then iterates from 2 up to the square root of `n` (inclusive), checking whether `n` is divisible by any integer in that range. If `n` is divisible by any of these integers, it returns `False`. However, if it isn't, it returns `True`, indicating that `n` is a prime number. This approach is efficient due to the optimized range of the loop and the use of the square root technique.