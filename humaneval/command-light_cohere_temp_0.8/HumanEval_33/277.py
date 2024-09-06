```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the item that are not divisible by three, while its values at the items that are divisible by three are equal to the values of the corresponding items of l, but sorted.
    #>>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 44, 55, 66, 77, 11, 22])
    [11, 22, 33, 44, 55, 66, 77, 11, 22]
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return sorted(l[3:], reverse=True) + l[:3]
```