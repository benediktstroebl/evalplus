```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer divisor of n that is less than n.
    """
    int m = 1
    while m <= n:
        if n % m == 0:
            return m
        m += 1
    return n
```