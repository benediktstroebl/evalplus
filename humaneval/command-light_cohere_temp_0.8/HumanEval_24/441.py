Here is a self-contained Python script that defines a function to find the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number divisible by n that is less than n itself.
    """
    numbers less than n but divisible by it, are 1, 2, 4, ..., n / 2, n / 4, n / 8, ...
    n is always the largest of these.
    """
example:
    >>> largest_divisor(15)
    5
    """
    return int((n - 1) // 2)
```