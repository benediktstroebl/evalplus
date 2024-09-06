```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    True
    >>> prime_fib(2)
    3
    False
    >>> prime_fib(5)
    89
    True
    >>> prime_fib(6)
    123
    False
    >>> prime_fib(8)
    13
    True
    >>> prime_fib(15)
    5635
    False
    >>> prime_fib(20)
    8888
    True
    """
    return (n <= 1) or ((n == 2) and (len([1] + [2] + [3])[1:])) or ((n % 3) == 0)
```