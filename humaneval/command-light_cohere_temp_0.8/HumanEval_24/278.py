```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not n % d))
```
The function returns the largest integer that evenly divides the given number, smaller than the given input n.