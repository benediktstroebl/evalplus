```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d))
```
This function returns the largest number that evenly divides the given number n, smaller than n. This is a way to solve the problem efficiently.