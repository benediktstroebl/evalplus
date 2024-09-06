```python
def largest_divisor(n: int) -> int:
    """
    Return the largest integer that divides n exactly
    """
    return (n+1) // max(n, 2)
```