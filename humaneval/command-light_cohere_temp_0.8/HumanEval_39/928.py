```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is also prime.
    >>> print(prime_fib(1))
    2
    True
    >>> print(prime_fib(2))
    3
    True
    >>> print(prime_fib(3))
    5
    True
    >>> print(prime_fib(4))
    13
    True
    >>> print(prime_fib(5))
    89
    True
    >>> print(prime_fib(6))
    24
    False
    >>> print(prime_fib(6))
    60
    False
    >>> print(prime_fib(7))
    81
    True
    >>> print(prime_fib(8))
    2428
    False
    >>> print(prime_fib(9))
    9999
    False
    """

The function checks for each Fibonacci number to see if it is prime or not, and then it returns the n-th Fibonacci number.  It only returns the adding numbers to the test suite.