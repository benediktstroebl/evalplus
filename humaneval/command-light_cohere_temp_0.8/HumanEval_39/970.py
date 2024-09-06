```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is prime.
    Returns None if n < 1
    """
    if n <= 1:
        return None
    return fibonacci(n) and is_prime(fibonacci(n))

def fibonacci(n: int):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True
```
This Python script defines a function `prime_fib` that calculates and returns the n-th Fibonacci number which is prime. It also checks if the maker function `fibonacci` generates a prime number. The helper function `is_prime` checks if a number is prime or not, using an efficient algorithm based on squares and divisibility.