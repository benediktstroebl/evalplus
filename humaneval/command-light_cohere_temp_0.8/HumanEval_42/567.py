```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l = list(map(lambda x: x+1, l))
    return l

# Test the function with various inputs
test_list = [1, 2, 3]
test_set = set([5, 3, 5, 2, 3, 5, 3])
test_dict = {'a': [1, 2, 3]}
test_custom = ['a', 'b', 'c']
test_iterable = (1, 2, 3)
test_none = None

# Call the function with different data types and validate the output
result_list = incr_list(test_list)
result_set = set(incr_list(test_set))
result_dict = incr_list(test_dict)
result_custom = incr_list(test_custom)
result_iterable = incr_list(test_iterable)
result_none = incr_list(test_none)

# Assertions
assert len(result_list) == 3
assert len(result_set) == 3
assert len(result_dict) == 3
assert len(result_custom) == 3
assert len(result_iterable) == 3
assert result_none == None
```