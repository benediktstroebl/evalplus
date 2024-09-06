```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number divisible by n, smaller than n"""
    return [7, 5, 3, 1].index(n % x for x in [7, 5, 3, 1]) + 1]
```