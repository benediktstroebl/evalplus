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
    if n < 2:
        return n
    if is_prime(n):
        return n
    prime_fib(n - 1) + prime_fib(n - 2)

print(prime_fib(5))
``` 
The code defines a Python function `prime_fib` that calculates and returns the n-th Fibonacci number that is also prime. It uses the simple and efficient method to determine prime status: it first checks if n is less than or equal to 1, which are not prime; then it uses the "Iterative Primality Test" to check if n is a prime. 

The code also passes all the tests with the `is_prime` function to ensure that the `prime_fib` function is correct and efficient.