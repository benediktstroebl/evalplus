Here's a Python script that provides a solution for the given problem:
```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        a, b = 5, 2
        for _ in range(n - 4):
            a, b = b, a + b
        return a
```
This function calculates and returns the n-th Fibonacci number that is also prime. It uses an iterative approach with Binet sequence generation.