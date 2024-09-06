```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and is also prime.
    Returns None if n < 0 or
    >>> prime_fib(1)
    2
    True
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(10)
    None
    """
    if n == 0:
        return None
    
    if n <= 1:
        return 2
    
    fib = 0
    fib_1 = 1
    fib_2 = 1
    
    for _ in range(2, n + 1):
        fib = fib_1 + fib_2
        fib_1, fib_2 = fib_2, fib + fib_2
        
    return fib
```