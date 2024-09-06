Here's the self-contained Python function that filters integers from a given list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list
test_values = ['a', 3.14, 5]
result = filter_integers(test_values)
assert len(result) == 3, "Filter failed"

# Test case 2: Filter integers from a list of strings
test_strings = ['1', 'abc', '2', '3']
result_strings = filter_integers(test_strings)
assert len(result_strings) == 3, "Filter failed"

# Test case 3: Filter integers from an empty list
test_empty = []
result_empty = filter_integers(test_empty)
assert result_empty == [], "Filter failed"
```
This function takes a list of values and returns a new list containing only the integers from the original list. The test cases provided help you using the function to ensure its correctness.