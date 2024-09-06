```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number that divides n exactly
    """
    return next((d for d in range(1, n+1) if not n%d) or d==n)
```