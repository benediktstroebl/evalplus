```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the third value, while preserving the original order of other values.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 3, 6, 9, 1, 7])
    [9, 10, 6, 3, 1, 7, 2]
    >>> sort_third([4, 2, 8, 12, 6, 10, 9])
    [2, 8, 6, 12, 10, 4, 9]
    """
    lst[::3] = lst[::3] + lst[1::3]
    lst[1::3] = lst[1::3] + lst[2::3]
    return lst
```  This function sorts a list l such that the third value of each list item is collected, while the first and second are kept intact and in the same order. It uses two operators : and :: to perform slicing and concatenation of lists.