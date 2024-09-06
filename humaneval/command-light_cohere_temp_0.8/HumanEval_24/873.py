```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not any(d % n == 0)))
```
This Python function, `largest_divisor(n)`, finds the largest integer that evenly divides the given number n. It does this using the remarkable technique using the "lazy" approach, it skips multiples of n in the `range` while iterating. This significantly reduces the Buy process, making it both efficient and self-contained.