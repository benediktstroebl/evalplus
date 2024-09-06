```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
The function largest_divisor returns the largest integer which evenly divides the given number n. It uses the