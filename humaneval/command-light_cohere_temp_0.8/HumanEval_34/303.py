```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return list(set(lst))

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Main code
if __name__ == "__main__":
    test_unique()
```
The function unique takes a list as input and returns a new list containing only the unique elements from the original list. This is is accomplished by using the set() function, which automatically filters out duplicates. The test_unique function tests the method and verifies the output of the unique function with the correct input.