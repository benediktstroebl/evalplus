```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer less than n that divides evenly."""
    return (n + 1) // max(2, int(n ** .5) + 1)
```