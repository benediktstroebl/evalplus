```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    seen = set()
    return list(seen)

def test_unique():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert unique(lst) == [0, 2, 3, 5, 9, 123]
```

You can use the test_unique function to verify the results of the unique function with your test list, or you can also extend the function with additional tests.