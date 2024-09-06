```python
def largest_divisor(n: int) -> int:
    return next(x for x in range(1, n+1) if any(n % x == 0)) or n
```
This function will return the largest integer that evenly divides the number n, ensuring that the result is less than or equal to n.