```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the values at positions not
    divisible by three are sorted to the same value.
    Args:
        lst (list)
    Returns:
        list, with values at positions divisible by three sorted to the same value,
        and other values sorted normally.
    """
Returns: list l'
    """
    lst[:] = sorted(lst, key=lambda x: x % 3)
    return lst
```