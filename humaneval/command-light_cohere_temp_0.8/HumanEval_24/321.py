```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest number that divides n evenly, smaller than n.
    """
    return n // // Even division will only be considered if divisor is less than n
    """
    if n < 2:
        return n
    else:
        return n // max(1, n - 2)
```