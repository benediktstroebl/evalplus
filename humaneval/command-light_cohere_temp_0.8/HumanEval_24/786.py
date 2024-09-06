```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly and is less than n.
    """
    smallest_integer_divisor(n)
    return n + smallest_integer_divisor(n)

def smallest_integer_divisor(n: int) -> int:
    """
    Returns the largest integer divisor less than n!
    """
    return 1 if n == 1
    i = 2
    while n % i == 0:
        i += 1
    return i
```