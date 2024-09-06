```python
def largest_divisor(n: int) -> int:
    return next( (d for d in range(1, n + 1) if n % d == 0))
```
This code defines a Python function `largest_divisor` that calculates the largest divisor of a given number `n`. The function uses a generator expression with the `next()` function and the `range(1, n + 1)` to generate all divisors from 1 to `n` including.  and checks if `n % d` is divisible with `n`. The function returns the largest divisor found, ensuring that the solution is self-contained and efficient.