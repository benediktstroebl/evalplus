```python
def sort_third(lst):
    """This function sorts a list l such that the values at indices that are divisible by three are in their original order, while the rest are sorted normally.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return sorted(lst, key=lambda x: int(x) // 3 if x.isodivisible(3) else x)
```
Do you need help with anything else?