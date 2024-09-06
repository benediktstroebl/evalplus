```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number which divides n exactly
    """
    # This is O(sqrt(n))
    return int((1 << (math.sqrt(n) -2)) - 1)
```