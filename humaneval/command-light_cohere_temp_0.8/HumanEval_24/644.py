```python
def largest_divisor(n: int) -> int:
    """
    Return the largest integer that divides n exactly without a remainder.
    """
    example:
    return 5
    """
    return n if n == 2 or n & 1 == 1 else n + 1
```