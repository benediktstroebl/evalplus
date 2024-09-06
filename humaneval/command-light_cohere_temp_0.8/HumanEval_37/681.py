```python
def sort_even(l: list):
    """Sorts a list of numbers so that the values at the even indices are equal, and the
    odd indices have their original values.

    Parameters:
    l (list): list of numbers
    Returns: list of numbers with the specified sorting
    """
    # copy the list
    l_copy = list(l)
    # sort the odd numbers first
    l_copy[::2:] = l_copy[:2]
    # sort the rest of the list
    l_copy[1::2] = l_copy[1:3] + l_copy[:2]
    # return the sorted list
    return l_copy
```