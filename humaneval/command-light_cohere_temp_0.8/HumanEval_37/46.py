```python
def sort_even(l: list):
    """Sorts list l so that the values at the even indices are equal to the values of the even indices of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 20, 30, 80, 100])
    [100, 80, 30, 20, 10]
    """
    return sorted(l, key=lambda x: x if x%2==0 else x-1)
```