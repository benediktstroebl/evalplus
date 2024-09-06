```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number that divides n evenly, 
    where n must be a positive integer.
    """
    example:
    >>> largest_divisor(15)
    5
    """
    return next((d for d in range(1, n+1) if n % d == 0))
```