```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    l = [3, 2, 4, 5, 6]
    return l[:] + [l[-1]] * [2] + l[-2:] + [l[-3]]
```