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
    fib = [2]
    for i in range(3, n + 1):
        fib.append(fib[-1] + fib[-2])
    return fib[n]

print(prime_fib(5))
```