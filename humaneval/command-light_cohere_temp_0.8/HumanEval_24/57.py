```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d))
```
This function uses the list comprehension to find the largest integer that evenly divides the given number n, and it returns the largest such integer less than n.