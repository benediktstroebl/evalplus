```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted."""
    l2 = [1, 2, 3]
    l3 = sort_even(l2)
    assert l3 == [1, 2, 3]
    l4 = [5, 6, 3, 4]
    l5 = sort_even(l4)
    assert l5 == [3, 6, 5, 4]
```