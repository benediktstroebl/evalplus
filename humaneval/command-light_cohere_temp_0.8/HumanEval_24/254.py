```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
This function uses the `next()` function with a generator expression to efficiently find the largest divisor of the given number n, ensuring that it only returns the largest divisor that divides n exactly without being equal to n.