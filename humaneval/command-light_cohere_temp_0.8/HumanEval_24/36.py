```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), -1)
```
This Python code defines a function `largest_divisor` that calculates and returns the largest divisor of the given integer `n`. The function utilizes a generator expression and the `next()` function to iterate through potential divisors from `range(1, n+1)` until it finds a divisor that does not create a remainder when divided into the original number. The function then returns - -1 to indicate that no such divisor exists for the given input.