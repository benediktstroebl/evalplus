```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number divisible by n that is less than n
    """
    return n // max((n - 1), 0)
```