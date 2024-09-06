```python
def unique(l: list):
    seen = set()
    return [x for x in l if x not in seen and not in [0]]

def test_unique():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [0, 2, 3, 5, 9, 123]
    assert unique(lst) == expected
```