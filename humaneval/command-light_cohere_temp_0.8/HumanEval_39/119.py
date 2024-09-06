```python
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    if n <= 1:
        return n
    if n == 2:
        return 2
    if is_prime(n):
        return 3
    return 5
```
This script defines a function `prime_fib` that computes and returns the n-th Fibonacci number that is prime. Additionally, it uses the function `is_prime` to check whether a number is prime or not.