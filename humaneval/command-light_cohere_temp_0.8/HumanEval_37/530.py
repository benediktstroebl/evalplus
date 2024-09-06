```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    """
    test:
    assert len(l) == 3
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([7, 8, 9]) == [7, 8, 9]
    assert sort_even([10, 10, 10]) == [10, 10, 10]
    """
```