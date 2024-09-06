```python
def sort_even(l: list):
    """Sorts the given list l such that the values at the even indices are equal to each other and are in order, while the odd indices are retained as they are.
    :>>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l.append(0)
    # Ensure that every index has a value
    l.sort(reversed(l))
    return l[:]
```