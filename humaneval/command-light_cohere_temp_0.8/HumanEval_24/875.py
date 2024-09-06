```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer that evenly divides the given number n, and is smaller than n."""
    return n if n % 1 else 2
    return n // 2
```