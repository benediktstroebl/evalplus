```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(l))

def test_unique():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert unique(lst) == [0, 2, 3, 5, 9, 123], "Error in unique function"

if __name__ == "__main__":
    test_unique()
```
The provided Python script defines a function `unique` that takes a list `l` as input and returns a new list containing only the unique elements from the original list. This is the unique elements are obtained using the `set()` function, which automatically filters out duplicates. The `test_unique` function contains a sample list and asserts that the `unique` function returns the correct unique elements.

This code provides a self-contained solution and test for the problem you provided.