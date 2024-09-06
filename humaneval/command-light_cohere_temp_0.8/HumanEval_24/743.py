```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly without a remainder.
    >>> largest_divisor(15)
    5
    """
    return next((i for i in range(1, n+1) if any(n % i == 0)))
```