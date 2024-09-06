```python
def sort_even(l: list):
    """Sorts a list l such that the values at the even indices are equal to the
    values of the even indices of l, but sorted.
    Parameters:
    l (list): A list of elements.
    Returns: A sorted list of l, with even elements sorted first.
    """

assert len(l) > 0:
    assert all(x % 2 == i for i, x in enumerate(l)),
    return sorted(l)
```