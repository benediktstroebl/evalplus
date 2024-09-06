```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if any(n % i == 0))
```
This function uses the `next()` function with a generator expression to efficiently find the largest number divisor that is less than or equal to the input number 'n'.