```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not n % d), None)
```
This Python code defines a function called `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`, smaller than `n`. This function uses a list comprehension with a generator expression `(d for d in range(1, n+1))` to generate all integers from 1 to `n` (inclusive) that are divisors of `n`. The `next()` function is used to extract the largest divisor from this list, returning `None` if no such divisor exists.