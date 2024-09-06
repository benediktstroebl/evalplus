```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if n % d == 0))
```
This Python code defines a function `largest_divisor` that calculates and returns the largest integer that evenly divides a given number `n`. It employs the `next()` function with a generator expression `(d for d in range(1, n + 1))` to iterate through numbers from 1 up to the given number, checking for divisibility by the modulo operation `n % d == 0`. This approach efficiently finds the largest divisor without the need for explicit recursion or list manipulation.