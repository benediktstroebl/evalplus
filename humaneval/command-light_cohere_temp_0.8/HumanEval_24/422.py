```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if n % d == 0))
```
This function will return the largest integer that evenly divides the given number n, smaller than n.