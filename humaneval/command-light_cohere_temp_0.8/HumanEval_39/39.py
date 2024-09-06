```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    """
    returns the generate a Fib first Fibonacci number
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        for i in range(2, n + 1):
            if is_prime(i) == True:
                return i
        return 0

def is_prime(n: int):
    """
    checks if the number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True
```

This script defines a function that calculates the n-th Fibonacci number which is also prime, and another function that checks whether a given number is prime or not. The first function returns the to the Fibonacci number for n, while the second function checks for primality.