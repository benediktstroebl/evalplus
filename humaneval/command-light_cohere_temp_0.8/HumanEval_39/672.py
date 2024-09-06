```python
import math
def prime_fib(n):
    """
    Returns n-th Fibonacci number that is also prime.
    >>> returns nth prime Fibonacci number.
    """ relies on a sqrt(5)
    """
    return math.sqrt(5) **n -n >= 2 and not is_prime(n))

def is_prime(n):
    """
    checks if number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
n = int(input("Enter a number to check: "))

if n < 2:
    print("Not prime")
else:
    if prime_fib(n):
        print("Yes, it is a prime number.")
    else:
        print("Not prime")
```