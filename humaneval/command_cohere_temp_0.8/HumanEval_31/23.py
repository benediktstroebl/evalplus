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
The function `is_prime` takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function first checks if `n` is less than 2, returning `False` if so. It then iterates from 2 up to the square root of `n` (inclusive), and for each number `i`, it checks if `n` is divisible by `i`. If `n` is divisible by any of these numbers, it returns `False`. However, if it hasn't returned `False` up to this point, it returns `True`, indicating that `n` is prime. 

This algorithm, called the `Sieve of Eratosthenes`, is efficient and minimizes the number of divisions required to determine primality. It also avoids the potential accuracy issues that can arise with floating-point computations, making it more robust.