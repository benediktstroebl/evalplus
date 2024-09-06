```python
def sort_third(lst):
    """Sorts list l such that values not divisible by three stay as they are, while values divisible by three are sorted to be the value of the corresponding index in lst."""
    return [x if (x % 3 == 0) else [x] for x in lst]

# Test the function
def test_sort_third():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
```