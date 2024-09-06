Here is a Python script with a self-contained function that solves the problem of finding the n-th Fibonacci number that is prime:
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
    fib = [0, 1]
    for i in range(2, n + 1):
        if is_prime(fib[-1] + fib[-2]):
            fib.append(fib[-1] + fib[-2])
    return fib[-1]

print(prime_fib(5))
```
This script defines a function `prime_fib` that calculates the n-th Fibonacci number that is also prime, it does so by iterating through the Fibonacci sequence and checking if each number is prime using the `is_prime` function. The function also handles the value of n.