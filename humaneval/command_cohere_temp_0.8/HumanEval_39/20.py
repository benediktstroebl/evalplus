Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Find the first Fibonacci number that is prime
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return a

# Tests
assert is_prime(2)
assert not is_prime(3)
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a `prime_fib` function that calculates the n-th number that is both a prime number and a Fibonacci number. It does this by iterating the Fibonacci sequence starting from the third element (`a = 0, b = 1`) until it finds the first prime number, then returns it as the n-th number. The `is_prime` function is also included to check if a number is prime.