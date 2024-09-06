```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd indic, while its values at the even indices are equal to the values of the even indicies of l, but sorted."""
    return l[:] if len(lst) % 2 == 0 else l[:len // 2] + [lst[len // 2]] + l[len :]
```