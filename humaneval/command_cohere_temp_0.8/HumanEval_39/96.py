Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    """
    # Initialize two variables for the first two Fibonacci numbers
    a, b = 0, 1
    count = 0

    while True:
        # Check if the next Fibonacci number is prime
        if is_prime(a):
            count += 1
            if count == n:
                return a
        
        # Move to the next Fibonacci number
        a, b = b, a + b

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a `prime_fib` function that generates the n-th Fibonacci number that is also prime. It does this by iteratively generating Fibonacci numbers and checking if each number is prime using the `is_prime` function. Once the count of prime Fibonacci numbers reaches `n`, it returns the corresponding Fibonacci number. The script includes a separate `is_prime` function to check if a number is prime or not.