```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test the function with some examples
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([]) == []
    assert unique([-100, 100]) == [-100]
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4]
test_unique()
```