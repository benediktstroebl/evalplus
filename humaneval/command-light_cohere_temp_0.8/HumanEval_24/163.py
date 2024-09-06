```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer dividing n without leaving a remainder.
    """
    return n //
    """/n 
    """
def test_largest_divisor(n):
    return n > 0 and all(d <= n // 2 for d in range(1, int(n)**0.5))
```