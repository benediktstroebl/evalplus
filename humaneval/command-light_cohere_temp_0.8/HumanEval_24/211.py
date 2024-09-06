```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer that evenly divides the given number n,
    ensuring it is less than n
    """
    return max(x for x in range(1, n+1) if x <= n and n % x == 0)
```