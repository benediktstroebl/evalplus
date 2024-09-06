```python
def max_element(lst):
    return max(lst)

# Test the function with a list of numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(test_list)
assert result == 123

# Test the function with a list of strings
test_strs = ["this", "is", "a", "test", "string"]
result = max_element(test_strs)
assert result == "is"
```