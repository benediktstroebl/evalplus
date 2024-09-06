```python
def sort_third(lst):
    """Returns a list l's such that all values divisible by three are sorted to the front of l."""
    return [x for x in lst if x % 3 == 0] + [x for x in lst if x % 3 != 0]

# Test
def test_sort_third():
    lst = [5, 6, 3, 4, 8, 9, 2]
    assert sort_third(lst) == [2, 6, 3, 4, 8, 9, 5]
```