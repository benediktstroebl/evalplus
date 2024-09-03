```python
def sort_even(l: list):
    """Sorts the values of a list l at the even indices only.

    Args:
        l (list): Target list to be sorted.

    Returns:
        list: A new list with even indices sorted and odd indices unchanged.
    """
    l_even = l[::2]
    sorted_even = sorted(l_even)
    result = l.copy()
    result[::2] = sorted_even
    return result
```