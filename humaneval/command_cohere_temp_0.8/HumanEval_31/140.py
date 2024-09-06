Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number `n` is less than 2, returning `False` immediately. It then iterates from 2 up to the square root of `n` (inclusive), and for each iteration, it checks if the current number evenly divides the given number `n`. If a divisor is found, it returns `False`, indicating that the number is not prime. If no divisors are found, it returns `True`, indicating that the number is prime.

This approach is efficient as it only needs to check potential divisors up to the square root of `n`. Numbers greater than the square root of `n` will have a multiple that's smaller than n and therefore don't need to be checked.