```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer less than n that divides it without a remainder."""
    if n <= 1:
        return n
    else:
        return(n // max(n - 1, 1))
```