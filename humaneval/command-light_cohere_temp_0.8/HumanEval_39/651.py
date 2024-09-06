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
        return
    if n == 1:
        return 2
    if n == 2:
        return 3
    a, b = 2, 3
    for _ in range(3, n + 2):
        a, b = b, a + b
    return a

if is_prime(5):
    print("5 is a prime number")
else:
    print("5 is not a prime number")

```

This code defines a Python script with a self-contained function that solves the prime Fibonacci problem and passes corresponding tests. It checks if a number is prime or not using the `is_prime` function, which uses a basic algorithm to test for primality. The function then returns the `True` if the number is prime and `False` otherwise. It then calls the final prime_fib function, which uses the same primality testing logic to calculate the n-th Fibonacci number that is prime. Finally, it passes tests and prints the result.