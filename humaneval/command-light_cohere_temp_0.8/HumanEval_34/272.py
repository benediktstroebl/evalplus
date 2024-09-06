```python
def unique(l: list):
    return list(set(l))

# Test the unique function with a sample input
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert test_unique == [0, 2, 3, 5, 9, 123]
```
This script defines a `unique` function that returns a new list containing only the unique elements from the input `list`. It uses the `set()` function to create a set from the input list, and then converts it back to a list to get the unique elements. The test suite uses this unique function with a sample input and asserts that the output matches the expected unique list with the specified elements.