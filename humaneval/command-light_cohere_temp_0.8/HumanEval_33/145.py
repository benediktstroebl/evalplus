```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 1, 2, 13, 3, 4, 5, 6])
    [10, 1, 2, 3, 4, 5, 6, 13]
    >>> sort_third([0, 0, 0, 0, 0, 0, 0, 0, 0])
    [0, 0, 0, 0, 0, 0, 0, 0]
    """

def test_sort_third():
    """Test if the function works correctly:
    l = [1, 2, 3]
    l.sort_third(l)
    assert l == [1, 2, 3]
    l = [5, 6, 3, 4, 8, 9, 2]
    l.sort_third(l)
    assert l == [2, 6, 3, 4, 8, 9, 5]
    l = [10, 1, 2, 13, 3, 4, 5, 6]
    l.sort_third(l)
    assert l == [10, 1, 2, 3, 4, 5, 6, 13]
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    l.sort_third(l)
    assert l == [0, 0, 0, 0, 0, 0, 0, 0]
```