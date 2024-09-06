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
```  This code defines a unique function that removes duplicate elements from an input list and returns a new list containing the unique elements in sorted order. The test_unique function then asserts that the output of the unique function matches the expected result for a given input list.