```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + [n]
    assert len(result) == len(l) + 1, "Length should be incremented"
    assert all(map(lambda x: x == x+1, result)), "Element should be incremented"
    return result

# Test the function
# Test with a list of numbers
test_list = [1, 2, 3]
result = incr_list(test_list)
assert test_list == result, "Expected list and test list to match"

# Test with nested list
test_nested = [ [1, 2, [3, 4]]
result = incr_list(test_nested)
assert test_nested == result, "Expected list and test list to match"

# Test with string
test_str = "Hello, World!"
result = incr_list([test_str])
assert test_str == result, "Expected list and test string to match"

# Test with nested list with strings
test_nested_str = ["World!", "!"]
result = incr_list(test_nested_str)
assert test_nested_str == result, "Expected list and test string to match"
```
The provided Python script defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. The function uses list comprehension and a new list [n] to add the length of the original list to the result. The function then performs a corresponding tests to ensure the correctness of the operation.

The script demonstrates the usage of the incr_list function with different types of lists and provides assert statements to verify the results against the expected values.