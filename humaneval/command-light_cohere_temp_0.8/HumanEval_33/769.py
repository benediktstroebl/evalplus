```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the item that are not divisible by three, while its values at the items that are divisible by three are equal to the values of the corresponding items of l, but sorted.

    Test:
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    l = list(map(int, l))
    l.sort(key= lambda x: 3==x%3)
    return sorted(l)
```