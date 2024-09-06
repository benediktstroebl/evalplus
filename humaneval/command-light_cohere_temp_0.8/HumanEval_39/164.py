```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    x = 0
    1
    y = 1
    for i in range(2, n + 1):
        x, y = y, x + y
    is_prime = True
    for p in range(2, int(math.sqrt(x)) + 1):
        if x % p == 0:
            is_prime = False
            break
    if is_prime:
        return x
    else:
        return None
```