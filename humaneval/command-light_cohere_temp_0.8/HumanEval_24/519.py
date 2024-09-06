```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not divmod(d, n).))
```
The function `largest_divisor` takes an integer `n` as input and returns the largest divisor of `n`. The function uses a generator expression to create a sequence of numbers from 1 to `n+1` and uses the `not divmod` function to check if the divisor divides the input number evenly.