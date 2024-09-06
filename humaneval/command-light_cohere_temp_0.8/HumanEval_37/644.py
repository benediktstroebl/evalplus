```python
def sort_even(lst):
    """This function sorts a list l such that the elements at odd indices are retained, and the elements at even indices are sorted.
    
    Args: 
    lst: list, list of integers or strings.
    """
   
    test: 
    Test case with a list lst of integers:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([4, 8, 2, 6])
    [2, 4, 6, 8]
    >>> sort_even([1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    """
    lst[::2] = sorted(lst[::2:])
    return lst
```