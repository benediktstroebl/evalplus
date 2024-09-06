```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer dividing n evenly, 
    that is less than n
    """
    return int((n + 1) // 2)
```