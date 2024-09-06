```python
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # using math.is_prime() function to check if n is a prime
    return math.is_prime(n)

def prime_fib(n):
    if n <= 1:
        return n
    if n <= 3:
        return 2
    if is_prime(n):
        return 3

    return 5

print(prime_fib(5))
```