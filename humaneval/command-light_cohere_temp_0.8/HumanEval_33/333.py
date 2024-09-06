```python
def sort_third(lst):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the item that are not divisible by three, while its 
    values at items that are divisible by three are equal to the values of the corresponding 
    items of l, but sorted.
    """
Example:
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return sorted(lst, key=lambda x: x // 3)
```