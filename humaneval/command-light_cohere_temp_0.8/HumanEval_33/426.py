```python
def sort_third(lst):
    """Returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at index that are divisible by three are equal to the values of the corresponding index of l, but sorted.

    Args:
        l (list):

    Returns:
        l' (list)
    """
    lst[::3] = lst[:::3]
    return lst
```