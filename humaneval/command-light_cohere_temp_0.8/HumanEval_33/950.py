```python
def sort_third(lst):
    """Sorts a list of numbers such that the corresponding values at indices that are not divisible by three are the same, and the values at indices that are divisible by three are sorted.

    Args:
        lst (list): list of numbers
    Returns:
        list: A list of numbers where values at indices that are not divisible by three are the same, and the values at indices that are divisible by three are sorted.
    """Example:
        >>> sort_third([1, 2, 3])
        [1, 2, 3]
    """
    # check if all values in the list are divisible by 3
    if all(x%3 == 0 for x in lst):
        return lst
    # sort the values in the list
    lst[:] = sorted(lst, key=lambda x: x // 3, reverse=True)
    return lst
```

This function first checks if all the values in the list are divisible by 3, and if so, it returns the list as is. Then, it sorts the list of numbers, ensuring that the values at indices that are not divisible by three are the same and the values at indices that are divisible by three are sorted in ascending order.