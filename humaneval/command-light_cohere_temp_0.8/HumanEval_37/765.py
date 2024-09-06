```python
def sort_even(lst):
    """Sorts the list l such that all odd indexes are retained, and the even indexes are sorted"""
    return [x if i%2 == 0 else sorted(lst)[i] for i, x in enumerate(lst)]

# Test
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```