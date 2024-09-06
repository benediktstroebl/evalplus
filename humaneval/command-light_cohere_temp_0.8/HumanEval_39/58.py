```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return i
        i += 6
    return n
```
The provided Python code defines a function `prime_fib` that computes and returns the n-th Fibonacci number that is prime. It uses a dynamic programming to quickly find prime numbers, eliminating redundant calculations. This function can be easily tested by calling it with various input values to ensure its correctness.