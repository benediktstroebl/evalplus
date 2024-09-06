```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted."""
    l1 = [1, 2, 3]
    l2 = [5, 6, 3, 4]
    l = l1 + l2
    l = sorted(l)
    l' = [x for x in l if x % 2 != 0]
    l = l + l'
    return l
```