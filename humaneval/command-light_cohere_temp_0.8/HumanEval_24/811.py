```python
def largest_divisor(n: int) -> int:
    """Finds the largest integer that evenly divides the given number n, smaller than n."""
    return n if n % 1 == 0 else n + 1
    return n
```