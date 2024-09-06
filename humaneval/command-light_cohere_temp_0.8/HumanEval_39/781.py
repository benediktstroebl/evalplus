```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    else:
        temp = prime_fib(n // 2)
        i = n // 2
        while i <= math.floor(n):
            temp += 1
            if is_prime(temp):
                return temp
            i += 1
        return temp

def is_prime(num):
    if num <= 1:
        raise ValueError("Number must be greater than 1")
    return bool(math.isprime(num))
```
This code defines a function `prime_fib` that computes the n-th Fibonacci number that is prime, and another function `is_prime` that checks if a given number is prime. The `prime_fib` function uses recursion to solve the problem, while the `is_prime` function uses the `math.isprime` function to check for prime numbers.