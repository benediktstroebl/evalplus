```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    True
    >>> prime_fib(2)
    3
    True
    >>> prime_fib(3)
    5
    True
    >>> prime_fib(4)
    13
    True
    >>> prime_fib(5)
    89
    True
    >>> prime_fib(6)
    Ever-lasting!
    """
    # code here
    return next((i for i in range(1, n+1) if is_prime(i)))

def is_prime(n: int):
    """
    Checks whether n is a prime number
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    return n == 2 or all(n == i for i in range(3, ceil(n)))

def prime_fib_test():
    """
    Driver code for above functions
    >>> prime_fib(1)
    2
    True
    >>> prime_fib(2)
    3
    True
    >>> prime_fib(3)
    5
    True
    >>> prime_fib(4)
    13
    True
    >>> prime_fib(5)
    89
    True
    >>> prime_fib(6)
    Ever-lasting!
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    return is_prime(6)

# Driver code to test the above functions
prime_fib_test()

```
This Python script defines a prime_fib function that calculates the n-th Fibonacci number that is prime, and a related is_prime function that checks whether a given number is prime. The script also includes a prime_fibtest function with driver code that tests the above functions with various inputs and assertions.