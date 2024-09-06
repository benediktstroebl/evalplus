```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    if n <= 1:
        return n
    if n % 2 == 0 or n % 3 == 0:
        return False
    fib_prev, fib_curr = 0, 1
    for _ in range(2, n + 1):
        fib_curr = fib_prev + fib_curr
        if fib_curr > 1.414:
    return False
```