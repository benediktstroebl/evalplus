```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([1, 2, 3, 4, 5])
    [1, 2, 3, 4]
    >>> sort_even([10, 11, 12])
    Traceback (most recent call last):
    ...
    ValueError: element 11 is not iterable
    """
def test_sort_even():
    l = [1, 2, 3]
    assert sort_even(l) == [1, 2, 3]
    l = [5, 6, 3, 4]
    assert sort_even(l) == [3, 6, 5, 4]
    l = [1, 2, 3, 4, 5]
    assert sort_even(l) == [1, 2, 3, 4]
    l = [10, 11, 12]
    with pytest.raises():
        assert sort_even(l) == [10, 11, 12]
```