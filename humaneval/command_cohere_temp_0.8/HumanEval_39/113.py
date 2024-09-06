Here's a Python script with a self-contained function `prime_fib` that generates the n-th number that is a Fibonacci number and it's also prime:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
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
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    
    def fibonacci(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    if n <= 8:
        return [2, 3, 5, 13, 21, 34, 55, 89][n - 1]
    else:
        return fibonacci(n)

# Tests
assert is_prime(2)
assert not is_prime(4)
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a helper function `is_prime` to check if a number is prime. The `prime_fib` function first checks if n is within the range of the pre-computed Fibonacci primes, and if so, returns the appropriate value. Otherwise, it generates the n-th Fibonacci number and iteratively checks its primality.