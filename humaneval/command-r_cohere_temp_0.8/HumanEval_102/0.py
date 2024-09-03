```python
def choose_num(x, y):
    """Returns the largest even integer in the range [x, y] or -1 if none exist.

    Args:
        x (int): Lower bound of the range.
        y (int): Upper bound of the range. Must be greater than x.

    Returns:
        int: Largest even integer in the range [x, y] or -1.
    """
    if y < x:
        raise ValueError("Invalid input range")
    even_numbers = [num for num in range(x, y + 1) if num % 2 == 0]
    if even_numbers:
        return max(even_numbers)
    else:
        return -1
```