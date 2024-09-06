```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n,
    that divides n evenly.
    """
    return n //%divisors(n) + 1
```