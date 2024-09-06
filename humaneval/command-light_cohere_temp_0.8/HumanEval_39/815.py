```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        # Calculate n-th Fibonacci number
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b
```