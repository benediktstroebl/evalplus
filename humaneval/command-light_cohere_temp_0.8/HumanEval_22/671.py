Here's a self-contained Python function that filters integers from a list of mixed values:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with a variety of inputs and verify the output
# Test 1: List of strings (should return [] because none are integers)
test_1 = [u'a', 3.14, 'five', 'abc123', 1, 2, 3]
assert filter_integers(test_1) == [], "Test 1 failed"

# Test 2: List of mixed integers and non-integers
test_2 = [1, 2, 3, 'abc', {}, []]
assert filter_integers(test_2) == [1, 2, 3], "Test 2 failed"

# Test 3: List of only integers
test_3 = [5, 3, 7, 9, 1, 4]
assert filter_integers(test_3) == [5, 3, 7, 9, 1, 4], "Test 3 failed"
```

This function takes a list of values as input and returns a new list containing only the integers from the input. The tests verify that function's expected behavior by checking if it returns the correct output for each list of inputs.