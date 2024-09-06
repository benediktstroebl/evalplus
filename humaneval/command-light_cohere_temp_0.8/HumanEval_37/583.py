```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Use insertion sort to sort the list with even indices
    even = [x for x in l if x % 2 == 0]
    for i, j in enumerate(even):
        l[i], l[j] = l[j], l[i]
    return l
```