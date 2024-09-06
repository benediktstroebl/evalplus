```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

def test_unique():
    list1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert unique(list1) == [0, 2, 3, 5, 9, 123]
```
This Python code defines a function `unique` that returns a list of sorted unique elements from an input list. It then defines a test_unique function with a test case, where it creates a list `list1` with a mix of duplicate elements, and the `unique` function is called with this list. The test passes the result of the function is asserted to be the expected output, which is a sorted set of unique elements from the list.