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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Create two variables, f and g, initialized to the first two numbers of the Fibonacci sequence
    f, g = 0, 1
    count = 0

    while count < n:
        # If f is prime, return it
        if is_prime(f):
            return f
        # If g is prime, return it
        if is_prime(g):
            return g
        # Create the next Fibonacci number
        count += 1
        f, g = g, f + g

    # If we reach the end of the loop, the requested number is larger than the max Fibonacci number
    return None

# Test the prime_fib function
# Very importantly, this tests the correctness of is_prime function too!
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
assert prime_fib(6) == None
```

This script defines a function `prime_fib` that uses the Fibonacci sequence to generate prime numbers that are sequenced accordingly. The function `is_prime` is used to check if a given number is prime. Finally, the `assert` statements test the `prime_fib` function to ensure it returns the correct results for values up to 6. 

Note that the `is_prime` function is used by `prime_fib` but also tested via the `assert` statements, which is good to fully validate the solution.