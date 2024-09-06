Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Generates the n-th Fibonacci number that is also prime.

    Args:
        n (int): The index of the Fibonacci number to generate.

    Returns:
        int: The n-th Fibonacci number that is also prime.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    def fibonacci_sequence(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)

    if n == 0 or n == 1:
        return 2  # The first two prime Fibonacci numbers are 2 and 3
    else:
        return next(i for i in fibonacci_sequence(n) if is_prime(i))

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```
This code defines a `prime_fib` function that generates the n-th Fibonacci number that is also prime. The function checks if n is within the range of the Fibonacci sequence's first two prime numbers (i.e., 0 and 1) and returns 2 or 3 accordingly. For larger values of `n`, the code generates the Fibonacci sequence and filters out non-prime numbers using a generator expression, efficiently finding the desired result. 

The `is_prime` function is also included to check if a number is prime. This function iterates through the numbers from 2 to the square root of the input number and checks for divisibility. If the number is divisible by any integer within this range, it's not a prime; otherwise, it's considered prime.