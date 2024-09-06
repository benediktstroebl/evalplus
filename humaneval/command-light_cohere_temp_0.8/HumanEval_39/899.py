Here is a Python script with a self-contained function that solves the Fibonacci prime problem:
```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        if is_prime(a):
            b = a
        a += 1
    return b

def is_prime(n: int):
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

This script defines a function `prime_fib` that calculates the n-th Fibonacci prime number and returns it. The `is_prime` function checks if a number is prime or not. It uses a simple and efficient trial-based algorithm to test for primality.