```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

def test_unique():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [0, 2, 3, 5, 9, 123]
    assert unique(lst) == expected
```