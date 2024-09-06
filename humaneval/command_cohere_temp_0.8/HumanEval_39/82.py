Here's a Python script with a self-contained function `prime_fib` that generates the n-th number that is a Fibonacci number and it's also prime:
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
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer.")
    count = 0
    fib_counter = 2
    max_fib_counter = 1000
    while True:
        if is_prime(fib_counter):
            count += 1
        fib_counter = fib_counter[-1] + fib_counter[1]
        if count == n:
            return fib_counter
        if fib_counter > max_fib_counter:
            raise RuntimeError("Reached maximum Fibonacci number.")

# Tests
assert prime_fib(1) == 2, "First prime Fibonacci number wrong"
assert prime_fib(2) == 3, "Second prime Fibonacci number wrong"
assert prime_fib(3) == 5, "Third prime Fibonacci number wrong"
assert prime_fib(4) == 13, "Fourth prime Fibonacci number wrong"
assert prime_fib(5) == 89, "Fifth prime Fibonacci number wrong"
```

This script defines a utility function `is_prime` to check if a number is prime. The `prime_fib` function uses a Fibonacci sequence to generate prime numbers and it raises a `ValueError` if `n` is not a positive integer and it raises a `RuntimeError` if it reaches a maximum Fibonacci number threshold to ensure this won't get stuck in an infinite loop generating non-prime Fibonacci numbers. 

The script also includes assertions to verify the correctness of the `prime_fib` function for specific test cases.