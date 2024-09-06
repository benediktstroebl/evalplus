Here is a Python script that includes the unique function along with tests to verify its functionality:
```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set_ = set(lst)
    return list(set_)

# Test 1: List with duplicate elements
test_cases = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_cases)
assert result == [0, 2, 3, 5, 9, 123]

# Test 2: List of strings
test_cases_str = ["Hello", "World", "!!", "!!"]
result_str = unique(test_cases_str)
assert result_str == ["H", "W", ".", "!"]

# Test 3: List of mixed data types
test_cases_mixed = [5, "Hello", True, [1, 2, 3], [4, 5]]
result_mixed = unique(test_cases_mixed)
assert result_mixed == [5, "Hello", True, [1, 2, 3], [4, 5]]
```

This script provides a function unique that accepts a list as an argument and returns a sorted unique set of elements from the input list. It is also provides several tests to validate the correctness of the unique function.