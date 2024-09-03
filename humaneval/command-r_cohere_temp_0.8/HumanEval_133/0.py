```python
def sum_squares(lst):
    """Returns the sum of squared numbers in the list after rounding each element to the upper integer value.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: Sum of squared numbers.
    """
    return sum(int(x) ** 2 for x in lst)
```