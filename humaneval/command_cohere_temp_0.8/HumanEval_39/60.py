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
    Generates the n-th Fibonacci number that is also prime
    """
    if n < 1:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    # Start with the first two Fibonacci numbers
    a, b = 0, 1
    count = 3

    while not is_prime(a) or not is_prime(b):
        # Calculate the next Fibonacci number
        a, b = b, a + b
        
        # Increment count if both numbers are prime
        if is_prime(a) and is_prime(b):
            count += 1
        
        # Check if we've generated enough Fibonacci numbers
        if count == n:
            return b
    
    return None

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a function `prime_fib` that generates the n-th Fibonacci number that is also prime. The function first checks if `n` is less than 2, returns 2 if `n` is 1, and returns 3 if `n` is 2 as the first two prime Fibonacci numbers. It then enters a loop where it generates the next Fibonacci number if it is not prime, and increments the count if it is prime. Once the count reaches `n`, it returns the `b` value as the n-th prime Fibonacci number.  The `is_prime` function is provided to check if a given number is prime.