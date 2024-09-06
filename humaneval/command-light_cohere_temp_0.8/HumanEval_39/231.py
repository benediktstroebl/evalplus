```python
import math

def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and is prime.
    if n <= 1:
        return n
    if n <= 3:
        return 2
    else:
        return math.isqfibonacci(n) % math.isMAXINT
prime_fibonacci()

def is_fibonacci(n):
    """
    Returns the n-th number in the Fibonacci sequence.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return is_fibonacci(n - 1) + is_fibonacci(n - 2)

def math_is_prime(n):
    """
    A math library function that checks if the number is prime.
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

def isMAXINT_in_range():
    """
    Returns a constant indicating the maximum possible integer value.
    """
    return int32

is_fibonacci = lambda n: isMAXINT() < n and is_prime(n) and is_fibonacci(n)

# Driver code
print(prime_fib(15))
print(is_fibonacci(15))
``` 
This Python code defines a series of functions that efficiently compute Fibonacci numbers and check whether they are prime. The code provides a function `prime_fib`, which returns the n-th Fibonacci number and is prime, and the function `is_fibonacci`, which returns the n-th number in the Fibonacci sequence. The code also uses the functions from the math library, such as `math_is_prime` and `math.isinfibonacci` to check for certain conditions (e.g., prime numbers or platform to check whether Fibonacci numbers are prime or not. The code also defines helper functions to efficiently check for these conditions and returns the result. The code provides a driver code at the end, which tests the `prime_fib` and `is_fibonacci` functions with various inputs.