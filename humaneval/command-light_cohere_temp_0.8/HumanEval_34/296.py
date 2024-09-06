```python
def unique(l: list):
    return list(set(l))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```

This code defines a function unique that returns a list containing only the unique elements from an input list. The test_unique function tests the to ensure that the unique function works correctly with the provided input.