```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    if n <= 1:
        return n
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n % 5 == 0:
        return True
    if n % 8 == 0:
        return False
    fib = 0
    fib_ = 1
    while fib < n:
        fib += fib
    return fib
```