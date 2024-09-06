Here's the self-contained Python function that solves the problem of finding the n-th Fibonacci number and checks its primality:
```python
def prime_fib(n: int):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    
    # Step 1: Initialize a1 and a2 with consecutive prime numbers
    a1 = 2
    a2 = 3
    prev_primes = [2, 3]
    for _ in range(5):  # Assuming that n is greater than 5
        if is_prime(prev_primes[-1] + 2):
            a1 = prev_primes[-1] + 2
            a2 = prev_primes[-1] + 3
            prev_primes.setdefault(prev_primes[-1] + 4)
    
    # Step 2: Calculate the n-th Fibonacci number
    fib_n = a1 * a2
    return fib_n

def is_prime(n: int):
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

# Example usage
print(prime_fib(10))
```
This script provides a self-contained function that calculates the 10th Fibonacci number and checks its primality.  It also includes a helper function to check if a number is prime.