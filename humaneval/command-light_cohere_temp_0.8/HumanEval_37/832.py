```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    l = [1, 2, 3]
    return l[:] + [x+1 for x in l] + l[-1:]
```