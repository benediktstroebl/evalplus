```python
def unique(lst):
    return list(set(lst))

# Test cases
test_unique = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 5, 2, '123', 'abc'],
    [5, 3, 7, [1, 2, 3]]
]

for item in test_unique:
    assert unique(item) == set(item), f"Failed for {print(item)}"
```

This script defines a function unique that returns a list of unique elements from a given list. It is designed to use the set() to remove duplicates and then convert it back to a list. The test suite provides a set of test cases for the unique function, and each test case includes a list of elements to process and the expected unique list. The test function also includes some edge cases with non-list inputs to ensure proper handling.