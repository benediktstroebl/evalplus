```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if not n % x))
```
This Python function named `largest_divisor` takes an integer `n` as input and returns the largest integer that divides evenly into `n`. This function uses a generator expression to find all numbers from 1 to `n` (inclusive) and returns the largest one that does not leave a remainder when dividing `n` by it.  The largest divisor of `n`.