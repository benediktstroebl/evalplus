```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.

    Args:
        n (int): The position of the desired Fibonacci number.

    Returns:
        int: Desired Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
```