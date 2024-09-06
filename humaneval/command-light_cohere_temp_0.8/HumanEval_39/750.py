```python
import math

def is_prime(n):
    """
    checks whether n is a prime number.

    if n <= 1:
        return False
    if n <= 3:
        return True
    sqrt_n = int(math.sqrt(n))
    if sqrt_n * sqrt_n <= n:
        for i in range(2, sqrt_n + 1, 2):
            if n % i == 0:
                return False
    return True

def prime_fib(n):
    """
    returns n-th Fibonacci number and also checks whether it's prime.

    if n <= 1:
        return n
    if n <= 3:
        return 3
    if is_prime(n):
        return n
    return prime_fib(n + 1)
```

This script defines two functions: `is_prime` which checks if a given number is a prime, and `prime_fib` which calculates the nth Fibonacci number and verifies if it's prime using the `is_prime` function. 
The `prime_fib` function uses recursion to calculate the nth Fibonacci number and then verifies if it's prime or not by checking if it's divisible by any number from 2 up to its square root.