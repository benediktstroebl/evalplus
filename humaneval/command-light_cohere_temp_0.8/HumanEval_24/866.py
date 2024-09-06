```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer that divides n exactly without a remainder.
    """
    for i in range(1, n//2 + 1):
        if n % i == 0:
            return i
    return n
```