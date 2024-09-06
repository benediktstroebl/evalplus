```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.

    Parameters:
        l (list): the list of numbers, to be sorted in even indices
    Returns:  l' (list): the list with elements at even indices sorted
    """
    l = [5, 6, 3, 4]
    return l[:][::2] + l[1::2]
```