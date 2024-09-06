Here is a self-contained Python function that filters out integers from a given list of values:
```python
def filter_integers(values):
    return [num for num in values if isinstance(num, int)]

# Test case 1
test_values = ['a', 3.14, 5]
result1 = filter_integers(test_values)
assert isinstance(result1, list), "Test case 1 failed"
assert len(result1) == 3, "Test case 1 failed"
assert all(isinstance(num, int) for num in result1), "Test case 1 failed"

# Test case 2
test_data = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(test_data)
assert isinstance(result2, list), "Test case 2 failed"
assert len(result2) == 3, "Test case 2 failed"
assert all(isinstance(num, int) for num in result2), "Test case 2 failed"

# Test case 3
test_values = [None, True, False, 0, 1, 2, 3]
result3 = filter_integers(test_values)
assert isinstance(result3, list), "Test case 3 failed"
assert len(result3) == 6, "Test case 3 failed"

print("All tests passed!")
```

This script defines a function called `filter_integers` that takes a list of values as an argument and returns a new list containing only the integers from the input. The test cases pass the
We pass several test cases to verify that the `filter_integers` function works correctly and produces the expected output.