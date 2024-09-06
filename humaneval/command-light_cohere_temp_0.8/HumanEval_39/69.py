```python
import math

def is_prime(n):
    """
    Check if n is prime
    """
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
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        return 2
    if n == 2:
        return 3
    a, b = 3, 5
    for _ in range(n - 2):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print(is_prime(5))
    print(prime_fib(5))
``` 
This code provides a function that checks if a number is prime, and another one that calculates the n-th Fibonacci number and determines if it's prime or not.  The main function calls these functions and prints the results.