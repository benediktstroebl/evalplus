```python
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    >>> prime_fib(6)
   acyclic
    """
    if n <= 1:
        return n
    if n <= 3:
        return 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    return True  # All other values of n are prime
```