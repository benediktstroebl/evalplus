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

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_fib, curr_fib = 0, 1
    for _ in range(n - 2):
        prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
    
    return prev_fib if is_prime(prev_fib) else curr_fib if is_prime(curr_fib) else None
```

This script defines a function `prime_fib(n)` which calculates the n-th Fibonacci number that is also a prime number. It uses an inner loop to calculate the Fibonacci numbers and an outer loop to iterate and find primes. 

The `is_prime(n)` function is also included to check if a number is prime or not. 

Note that the script assumes n is a positive integer and that prime numbers larger than circulation under 100,000,000,000,000,000 may not be accurate due to computational and mathematical factors.