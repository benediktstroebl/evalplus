```python
def unique(lst):
    """Sorts and returns unique elements from a list"""
    set1 = set(lst)
    return list(set1)

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Run the function and tests
if __name__ == "__main__":
    test_unique()
```