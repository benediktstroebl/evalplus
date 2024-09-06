```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is prime.
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    else:
        return 2 + prime_fib(n - 2)
```