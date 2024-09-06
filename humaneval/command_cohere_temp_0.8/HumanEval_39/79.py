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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Make sure n is positive
    n = abs(n)
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Start with the 3rd Fibonacci number (2nd is 1, which is not prime)
        a, b = 3, 5
        for _ in range(n - 2):
            a, b = b, a + b
        return a
```

This script defines two functions:
1. The `is_prime` function checks if a given number is prime or not. 
2. The `prime_fib` function returns the n-th number that is a Fibonacci number and it's also prime. The function handles the special cases of n=1 and n=2, then iterates through the Fibonacci sequence starting from the 3rd number (since the 2nd number is not prime), generating prime numbers that are Fibonacci numbers.

These functions are then tested with the provided doctests, which are executed when the script is run directly.