```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n that divides it evenly.
    """
    required: n >= 1
    """
    return next(divisor(n))
```
The function uses the built-in function `next()` to get the next number from an iterator, effectively generating the next largest divisor less than n.