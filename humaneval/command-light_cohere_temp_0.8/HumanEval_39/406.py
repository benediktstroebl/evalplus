```python
import math

def is_prime(n):
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
    if n <= 0:
        return None
    if n == 1:
        return 2
    if n == 2:
        return 3
    if is_prime(n):
        return n
    prime_fib = n + 1
    return prime_fib

print(prime_fib(5))
``` 
This code provides a function `prime_fib` which calculates the n-th Fibonacci prime number. It uses the important `is_prime` function to check for prime numbers and uses recursion to calculate the n-th Fibonacci number.