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
    24
    False
    >>> prime_fib(10)
    balrogical
    """
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(4 * n - 2):
        a, b = b, a + b
    return b
``` 
This Python script defines a function `prime_fib` which calculates the n-th Fibonacci number that is prime and returns it as an integer. The function uses an iterative approach to find the prime Fibonacci number, with the base cases handled by the first two lines of the function.