```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 10, 20, 30])
    [10, 10, 20, 30]
    >>> sort_even([5, 6, 3, 4])
    [4, 5, 6]
    """
    lst = sorted(lst, key=lambda x: x%2)
    return lst
```  This script defines a function `sort_even` that takes a list as an argument and returns a list with the elements from the input list sorted in such a way that preserves the even indices.