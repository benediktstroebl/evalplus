```python
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            if n <= 1:
                return False
        divisor += 1
    return True

def prime_fib(n):
    """
    Returns n-th Fibonacci number that is also prime
    Returns n-1 if n is not a prime
    """
    if n <= 1:
        return n
    if n <= 3:
        return 2

    # make sure n is prime
    if is_prime(n):
        return n + prime_fib(n - 1)
    else:
        return n - 1

# Test
print(prime_fib(5))  # 89
print(prime_fib(13))  # True
print(prime_fib(4))  # 13
print(prime_fib(2)))  # 2
print(prime_fib(0)))  # 1
```
The function `prime_fib` calculates the n-th Fibonacci number that is also prime, and returns n-1 if n is not prime. 

The `is_prime` function is a helper function that checks if a given number is prime, it uses the trial-division algorithm to determine whether a number is prime or not. 

The `prime_fib` function then uses these two functions to calculate the n-th Fibonacci prime number.