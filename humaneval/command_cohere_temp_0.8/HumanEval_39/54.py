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

def prime_fib(n):
    if n <= 0:
        return None
    x, y = 0, 1
    for _ in range(n - 1):
        x, y = y, x + y
    if is_prime(x):
        return x
    return None

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a function `prime_fib` that returns the `n`-th number that is both a Fibonacci number and a prime number. It uses the `is_prime` function to check if a number is prime. The `prime_fib` function initializes `x` and `y` with the first two digits of the Fibonacci sequence and loops `n-1` times to calculate the `n`-th Fibonacci number. Finally, it checks if the number is prime using the `is_prime` function and returns it if it passes the test.