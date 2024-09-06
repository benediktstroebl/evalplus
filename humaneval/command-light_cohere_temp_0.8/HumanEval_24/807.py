```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number divisible by n that is less than n.
    """
    number = 1
    while n >= number:
        n, number = divmod(n, number)
    return n
```