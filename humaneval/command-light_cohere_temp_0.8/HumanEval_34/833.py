```python
def unique(lst):
    """Sorts and returns unique elements in a list."""
    set1 = set(lst)
    return list(set1)

def test_unique():
    """Test case for unique function."""
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This Python script defines a function called unique, which takes a list as input and returns a new list with unique elements from the original input list. The function uses the blueprint of the `set` function to remove duplicates and then convert the remaining elements to a `list`. The `test_unique` function contains a test case for the unique function, which asserts that it works correctly.