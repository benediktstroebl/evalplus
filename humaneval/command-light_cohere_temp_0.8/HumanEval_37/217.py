```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 20, 30])
    [10, 20, 30]
    """
    return l[:] + [x + y for x, y in zip(l[1:], l[0:])]

# Unit tests
def test_sort_even():
    test_list = [1, 2, 3, 4, 5, 6, 7]
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert sort_even(test_list) == expected
```