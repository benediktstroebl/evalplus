Here is a self-contained Python script that defines a function `largest_divisor(n: int)` that finds the largest divisor of a given number:
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