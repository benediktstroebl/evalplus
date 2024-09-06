```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.

    Args:
        l (list): list to be sorted

    Returns:
        l' (list): sorted list
    """
    l_copy = l.copy()
   
    list(set(l))
    l_copy.append(l.getitem(0))
    l_copy.sort()
    value, 1
    return l_copy
```