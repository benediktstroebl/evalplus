```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # initialize a new list l' to be equal to l
    l = [x for x in l]

    # loop through the list l and swap the values of even index with the values of the corresponding even index in l
    for i in range(len(l)):
        if i % 2 == 0:
            l[i], l[i + 1] = l[i + 1], l[i]

    # return the sorted list l'
    return l
```