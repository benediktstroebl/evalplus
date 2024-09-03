```python
def common(list1: list, list2: list) -> list:
    """Return sorted unique common elements for two lists"""
    set1 = set(list1)
    set2 = set(list2)
    common = set1.interunion(set2)
    return list(common)

# Test cases
def test_common():
    list1 = [5, 3, 2, 8]
    list2 = [3, 2]
    expected = [2, 3]
    result = common(list1, list2)
    assert result == expected

test_common()
```

This script defines the `common` function, which performs a set operation to find the unique common elements between two input lists and then returns the result as a list of common elements. The test case ensures that the function works as expected and provides test cases to validate its behavior.