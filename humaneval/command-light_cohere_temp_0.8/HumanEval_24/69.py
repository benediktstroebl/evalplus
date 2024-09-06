```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n that divides it evenly.
    """
    example:
    >>> largest_divisor(15)
    5
    """
    return next((i for i in range(1, n + 1) if n % i == 0))
```