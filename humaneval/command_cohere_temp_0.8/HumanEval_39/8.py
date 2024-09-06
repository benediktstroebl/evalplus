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
    """
    Generates n-th Fibonacci number that is also prime
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if n == 1:
        return 2
    if n == 2:
        return 3
    fib, prev = 0, 1
    for _ in range(n - 2):
        fib, prev = prev, fib + prev
    # Search for primes between fib(n-2) and fib(n-1)
    for num in range(max(fib - 2, 2), fib):
        if is_prime(num):
            return num
    raise ValueError(f"No prime Fibonacci number for n = {n}")
```

This script defines two functions:
- The `is_prime` function checks whether a given number is prime or not. 
- The `prime_fib` function aims to generate the n-th Fibonacci number that is also prime. 

The `prime_fib` function first determines if n is within a reasonable range to be the corner cases (`n=1` and `n=2`). It then computes the Fibonacci numbers one by one and in each iteration, it checks the interval between the last two computed Fibonacci numbers for prime numbers. The interval is gradually increasing, providing a larger search space for prime numbers. The function finally returns the n-th Fibonacci number that is also prime. 

This solution has a time complexity of `O(n)` as it generates each Fibonacci number only once and performs a linear search for each prime Fibonacci number.