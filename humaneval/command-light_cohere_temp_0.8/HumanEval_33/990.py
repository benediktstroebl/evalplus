```python
def sort_third(l: list):
    """Sorts a list l of integers so that values at indices that are not
    divisible by three are at the beginning. Values at indices that are divisible by three
    are sorted to match the values of the corresponding indices of l, but are
    moved to the end of the list."""
    l.sort_third(l)
    assert l == [1, 2, 3]
    assert l == [1, 2, 3]
    assert l == [2, 6, 3, 4, 8, 9, 5]
    assert l == [2, 8, 9, 6, 3, 4, 5]
```