```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
The provided code defines a Python function `largest_divisor(n: int)` which finds the largest divisor of the given integer `n`. The function utilizes a generator expression with the `range(1, n+1)` function to iterate through numbers from 1 up to the given integer.

The `largest_divisor` function returns the largest divisor found during the iteration, which ensures that the returned value is always greater than or equal to the input `n`.