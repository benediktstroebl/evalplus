```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    p, q = 2, 3
    for _ in range(2, n):
        while not math.isprime(p * q):
            p, q = q, p + q
        if p > 1:
            return p
    return -1  # This will return -1 if the function encounters a loop without finding a prime.
# Example the function with various input values. 
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: -1
print(prime_fib(10))  # Should raise an error: 10 is not a prime number
```