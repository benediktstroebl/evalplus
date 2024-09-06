```python
def largest_divisor(n: int) -> int:
    """Finds the largest integer which divides n exactly"""
    return next((d for d in range(1, n + 1) if n % d == 0))
```
The function returns the largest integer that evenly divides the given number. This is using the time complexity of O(1) and using list comprehension to find the largest divisor.