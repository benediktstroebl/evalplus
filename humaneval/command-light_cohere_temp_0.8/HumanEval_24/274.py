```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest number which divides n exactly and is smaller than n
    """
    return n // max(1, n - 1)
```