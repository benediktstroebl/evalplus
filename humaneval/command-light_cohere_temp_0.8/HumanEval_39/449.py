```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    else:
        a, b = 5, 2
        for _ in range(n - 4):
            a, b = b, a + b + 2
        return a
```
This Python code defines a function `prime_fib` that calculates the n-th Fibonacci number which is prime. It employs a specific logic to find the nth prime Fibonacci number.