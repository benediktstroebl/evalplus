```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly and is less than n.
    """
    required: n > 0
    return gcd(n, n-1)
```