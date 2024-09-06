```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even indic are equal
    to the values of the even indic of l, but sorted."""
    l = [1, 2, 3]
    l.sort_even()
    above [1, 2, 3]
    l.sort_even([5, 6, 3, 4])
    assert l == [3, 6, 5, 4]
    l = [5, 6, 3, 4]
    l.sort_even()
    above [5, 6, 3, 4]
    l.sort_even([7, 8, 9])
    assert l == [7, 8, 9]
```