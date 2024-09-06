```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted."""
    return l[:] if len(l) % 2 == 0 else l[:len // 2] + [l[-len // 2]:] + l[::len // 2]
```