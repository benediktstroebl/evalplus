```python
def unique(lst):
    return list(set(lst))

# Test the unique function
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_unique)
assert len(result) == 7  # Should be 7 unique elements

# Test passing elements
test_passing = [0, 2, 3, 5, 9, 123]
result_passing = unique(test_passing)
assert result_passing == test_passing  # Should be passing elements unchanged
``` 
This code defines a function `unique` that returns a list of unique elements from the input list `lst`. The test cases pass the function with a list of known values and compare the result with the expected list of unique elements. The `assert` statements at the both test cases ensure that the output of the `unique` function is correct for the given input.