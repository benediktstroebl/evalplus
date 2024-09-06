```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the items that are not divisible by three, while its values at the items divisible by three are equal to the values of the corresponding items of l, but sorted."""
    l = [1, 2, 3]
    l.sort_third(l)
    assert l == [1, 2, 3]
    l = [5, 6, 3, 4, 8, 9, 2]
    l.sort_third(l)
    assert l == [2, 6, 3, 4, 8, 9, 5]
```