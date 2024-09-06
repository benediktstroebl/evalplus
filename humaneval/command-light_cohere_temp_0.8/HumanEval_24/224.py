```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number divisible by n that is less than n.
    """
    number = n + 1
    while number > n:
        number //= 2
    return number
```