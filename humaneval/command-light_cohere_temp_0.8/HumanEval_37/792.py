```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even indic are equal
    to the values of the even indic of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 2, 8, 20])
    [8, 10, 2, 20]
    >>> sort_even([1, 2, 3, 4, 5])
    [1, 2, 3, 4]
    >>> sort_even([6, 7, 8, 9])
    [9, 8, 7, 6]
    """
    # Create a new list with the same elements but sorted by even index
    l_even = list(zip(*l))
    l_even.sort_even(l_even)
    return l_even
```  This function works by creating a new list with the same elements as the input list, but with the elements sorted by even index. It then uses the SO sorting algorithm to sort the elements in the new list by even index.