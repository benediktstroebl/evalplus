```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number which divides n exactly
    """
    return next((d for d in range(1, n+1) if n % d == 0))
```