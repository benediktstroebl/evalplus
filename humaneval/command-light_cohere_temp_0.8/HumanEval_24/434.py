```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer that evenly divides n, smaller than n"""
    return max((i) for i in range(1, n + 1) if n % i == 0)
```