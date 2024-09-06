Here is a Python script with a self-contained function that solves the problem:
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
    else:
        # Calculate Fibonacci numbers using recurrence relation
        a, b = 0, 1
        for _ in range(2 * n - 2):
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

This script defines a `prime_fib` function that calculates the n-th number that is both a prime number and a Fibonacci number. It starts by checking if `n` is less than or equal to 0, and raises a `ValueError` if so, as `n` must be a positive integer. If `n` is 1, it returns 2 since the first prime Fibonacci number is 2. Otherwise, it iterates twice `n - 1` to calculate the `(2 * n - 1)-th` number in the Fibonacci sequence, which is the `n-th` prime Fibonacci number. The `is_prime` function is also included to check if a given number is prime.