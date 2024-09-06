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
   awn
    >>> prime_fib(7)
   cot3
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n % 2 == 0:
        return 5
    for i in range(5, n + 1, 2):
        if n % i == 0:
            continue
        temp = prime_fib(i)
        if temp > 1 and temp <= sqrt(n):
            return temp
```