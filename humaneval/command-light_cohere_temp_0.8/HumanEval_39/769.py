```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is prime.
    >>> prime_fib(1)
    2
    True
    >>> prime_fib(2)
    3
    False
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
    27
    False
    >>> prime_fib(7)
    56
    True
    >>> prime_fib(8)
    144
    False
    >>> prime_fib(9)
    666
    True
    >>> prime_fib(10)
    Arvix
    True
    """
    return n == 10 or any(is_prime(i+1) for i in range(2, n))

def is_prime(n: int):
    """
    True if all(n == 1 or n == 2 or i <= sqrt(n) for i in range(3, int(n**0.5+1))
   
    """
Here we have a `prime_fib` function that returns the n-th Fibonacci number and checks if it is prime. We also have a other helper functions that help us to check if a given number is prime or not.