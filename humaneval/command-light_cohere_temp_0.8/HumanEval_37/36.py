```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd indic, while its values at the even indicies are equal to the values of the even indic of l, but sorted.

    >>> sorted(list([1, 2, 3]))
    [1, 2, 3]
    >>> sorted(list([5, 6, 3, 4]))
    [3, 6, 5, 4]
    """

    # create new list with elements at even index as sorted version of it
    l_even = l[:] + [x for x in l if x%2 == 0]

    # use sorted() function to sort l_even list and assign back to l
    l = l_even

    return l
```