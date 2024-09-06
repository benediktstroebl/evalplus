```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest integer that evenly divides the given number, 
    smaller than n
    """
    return int((n + 1) // 2)
```