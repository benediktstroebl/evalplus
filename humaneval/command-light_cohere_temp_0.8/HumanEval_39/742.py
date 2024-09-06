```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    else:
        a, b = 3, 5
        for _ in range(n - 2):
            a, b = b, a + b + 1
        return b
```
This function, `prime_fib`, calculates the nth Fibonacci number that is prime. It uses a important formula for prime Fibonacci numbers and implements it with a loop.

This code is self-contained and provides a solution to the given problem of finding prime Fibonacci numbers.