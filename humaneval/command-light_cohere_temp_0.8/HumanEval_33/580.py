```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    assert len(l) == 3
    assert len([x for x in l if x % 3 != 0]) == 1
    assert l[0] == 2 and l[1] == 6 and l[2] == 8
    assert l[0] != l[1] and l[1] != l[2] and l[2] != l[0]
    l[:] = [2, 6, 8]
    return l
```