```python
import math
def prime_fib(n):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    if n <= 1:
        return n
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Use Sieve of Eratosthenes to check for primality
    for i in range(2, int(math.sqrt(n)) + 1):
        if math.isq(i, n) == 0:
            return False
    return n
# Driver code
print(prime_fib(5))
```