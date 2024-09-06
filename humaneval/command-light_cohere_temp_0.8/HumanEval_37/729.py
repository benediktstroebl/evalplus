```python
def sort_even(l: list):
    return sorted(l, key=lambda x: int(x) if x.isdigit() else x.isdigit() and
 does not exist, so the default value will be used.

def test_sort_even():
    """This function takes no arguments and returns a boolean value"""
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```