```python
def unique(l: list):
    return list(set(l))

# Test the unique function with a list of mixed numbers
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_unique)
assert len(result) == 7  # Check that the length is correct
assert set(result) == set([0, 2, 3, 5, 9, 123])  # Check for uniqueness

# Test the function with a list of strings
test_strings = ["abc", "123", "abc", "xyz"]
result_strings = unique(test_strings)
assert len(result_strings) == 3  # Check the length again
assert set(result_strings) == set(["abc", "123", "xyz"])  # Check for uniqueness

# Test the function with a list of nested lists
test_nested = [[1, [2, 3], 4], [5], 6]
result_nested = unique(test_nested)
assert len(result_nested) == 4  # Check the length

# Test the function with complex data types
test_complex = [True, [42, (7, "g"), [42]]
result_complex = unique(test_complex)
assert len(result_complex) == 3  # Check the length again

# All tests passed successfully!
print("All tests passed!")
```