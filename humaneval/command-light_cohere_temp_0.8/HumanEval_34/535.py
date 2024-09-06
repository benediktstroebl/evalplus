```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    set1 = set(l)
    return list(set1)

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
The `unique` function takes a list `l` as input and uses the `set` function to convert it into a set. Then, it uses the unique function to retrieve the unique elements from the set and converts them back into a list. The test_unique function contains a test case that checks if the `unique` function works correctly with a sample input.