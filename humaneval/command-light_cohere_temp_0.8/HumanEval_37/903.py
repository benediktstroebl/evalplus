```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even indicies are equal
    to the values of the even indic of l, but sorted."""
    return [i for i in l if i % 2 != 0][::2] + [i for i in l if i % 2 == 0][::2]

# tests
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```