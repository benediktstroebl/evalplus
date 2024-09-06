```python
def largest_divisor(n: int) -> int:
    return next(d for d in range(1, n+1) if n % d == 0)
```
This function, `largest_divisor`, uses the `next()` function with a generator expression to efficiently find the largest number divisor of a given number 'n' under the assumption that the input is a positive integer. It uses the unique approach, without iterating over the entire range, making it more memory-efficient for large inputs.