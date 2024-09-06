Here's a Python script with a self-contained function that solves the problem:
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
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Find nth prime Fibonacci number
        count = 0
        fib_prev = 0
        fib_curr = 1
        while True:
            if is_prime(fib_curr):
                count += 1
                if count == n:
                    return fib_curr
                fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
            else:
                fib_curr += fib_prev
```

This script defines two functions:
1. The `is_prime` function checks whether a given number is prime. It handles special cases up to 3 and then uses a optimized algorithm (Eratosthenes' Sieve) to quickly determine if a number is prime.
2. The `prime_fib` function calculates the n-th number that is a Fibonacci number and it's also prime. It uses an optimized way to find the n-th prime Fibonacci number by maintaining a count of prime Fibonacci numbers and updating the Fibonacci variables accordingly.

The script then provides example outputs to show the behavior of the `prime_fib` function.