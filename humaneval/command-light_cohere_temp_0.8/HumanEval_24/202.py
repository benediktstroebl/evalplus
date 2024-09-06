```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest number which divides n exactly and is smaller than n
    Returns the largest divisor
    """
    return next((d for d in range(1, n+1) if n % d == 0))
```