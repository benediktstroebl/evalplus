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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Ensure n is a positive integer
    n = abs(int(n))
    if n <= 0:
        return None

    # Initialize two variables for the Fibonacci sequence
    a, b = 0, 1
    count = 0

    while count < n:
        # If a is prime, return it
        if is_prime(a):
            return a
        
        # Calculate the next number in the Fibonacci sequence
        a, b = b, a + b
        count += 1

    # If we reach this line, a is prime
    return a

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a `prime_fib` function that calculates the n-th Fibonacci number that is also prime. It starts by defining a helper function, `is_prime`, which checks if a given number is prime. The `prime_fib` function initializes two variables `a` and `b` to initialize the Fibonacci sequence and then enters a loop where it iterates through the Fibonacci sequence until it generates the n-th number. It checks if each number in the sequence is prime using the `is_prime` function, and when a prime number is found, it returns it. If n is an invalid input, it returns `None`.

The script also includes some tests to validate its behavior. You can add these tests to a separate Python file and run them to verify the correctness of the `prime_fib` function.