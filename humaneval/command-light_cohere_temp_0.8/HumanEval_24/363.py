```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if n % d == 0))
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n`. The function uses a generator expression to find the largest divisor by iterating from `d` from `1` up to `n`. The `next()` function is used to get the next value from the generator, ensuring that the function returns the largest divisor.