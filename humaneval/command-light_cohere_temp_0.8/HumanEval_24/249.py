```python
def largest_divisor(n: int) -> int:
    return next( (d for d in range(1, n + 1) if not n % d))
```
This Python script defines a function `largest_divisor(n: int)` that aims to find the largest divisor of the given integer `n`. The function uses a generator expression with the `next()` function and the range from 1 to `n + 1` to iterate over all potential divisors of `n`. The `next()` function returns the next value from the iterator, ensuring that we get the largest divisor that doesn't divide `n` evenly.