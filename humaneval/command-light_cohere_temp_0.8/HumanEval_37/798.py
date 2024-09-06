```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    Parameters:
    l (list): the list to be sorted
    Returns:
    l' (list): the list with the elements sorted in even index

    """
    l = list(l)
    l.insert(0, l[1])
    l = l[:0:-1]
    return l
```