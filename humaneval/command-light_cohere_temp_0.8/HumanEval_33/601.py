```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the index that are not divisible by three, while its values at the index that are divisible by three are equal to the values of the corresponding index of l, but sorted.

    Test suite:
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

def test_sort_third():
    l = [1, 2, 3]
    l.extend(3)
    assert l == [1, 2, 3]
    l = [5, 6, 3, 4, 8, 9, 2]
    l.extend(3)
    assert l == [2, 6, 3, 4, 8, 9, 5]
```