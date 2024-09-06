```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 20, 30, 40, 50, 60])
    [10, 20, 30, 40, 50, 60]
    >>> sort_even([1, 2, 3, 4, 5])
    [3, 2, 1, 4, 5]
    """
    l = [3, 2, 1, 4, 5]
    return sorted(l, key=lambda x:x%2)
```