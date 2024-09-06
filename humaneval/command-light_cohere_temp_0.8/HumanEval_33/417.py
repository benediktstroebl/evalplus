```python
def sort_third(lst):
    """This function sorts the list so that values not divisible by three appear first,
    while the other values are sorted normally.
    >>> [1, 2, 3]
    [1, 3, 2, 4, 6, 8, 9]
    """
    return sorted(lst, key=lambda x: x%3)
```