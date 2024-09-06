Here's a Python script with a self-contained function that checks whether a given number is prime or not:

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

This function takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The function uses an optimized trial of time by using a "square and double" strategy, which reduces the number of iterations required to find divisors of large numbers.

The function also includes some initial checks:
- If `n` is less than or equal to 1, it is clearly not a prime number.
- If `n` is less than 3, it is also not a prime number, as prime numbers greater than 2 are divisible by 3.

Finally, the function uses a simple loop to test divisors up to the square root of the number, and returns `True` if no divisors are found within this range.