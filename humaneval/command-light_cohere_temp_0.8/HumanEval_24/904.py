```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer which is a divisor of n and smaller than n.
    """
    example:
    return 5  # for 15
    """
    return max((i for i in range(1, int(n**0.5))))
```