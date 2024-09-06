```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer which divides n exactly
    """
    return max((i for i in range(1, int(n**0.25) if n % i == 0))
```