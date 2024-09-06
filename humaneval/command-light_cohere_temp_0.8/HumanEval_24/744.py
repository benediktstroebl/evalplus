```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer less than n that divides it evenly."""
    while n % 2 == 0:
        n += 1
    return n
```