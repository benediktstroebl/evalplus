```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        a, b = next((i for i in [a, b] if i > 1 and i % (a + b) == 0)), a + b
    return a

# Test case: pass test function
def test():
    assert prime_fib(5) == 89
    assert prime_fib(2) == 3
    assert prime_fib(6) == 28
    assert prime_fib(15) == 56
    assert prime_fib(4) == 13
    assert prime_fib(3) == 5
```
The provided code defines a function `prime_fib` that returns the n-th Fibonacci number that is also prime. It uses an iterative approach to generate prime Fibonacci numbers by repeatedly updating the values of two consecutive Fibonacci numbers if their previous value is greater than 1 and its ratio is equal to or smaller than the square of the sum of the previous two values.