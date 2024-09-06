```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    l_even = [x for x in l if x % 2 != 0]
    l_sorted = l[:] + [x if x in l_even else l_even[::-1] for x in l[1:]]
    return l_sorted
```