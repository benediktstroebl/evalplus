```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with a list of values
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

result = get_positive(test_list)
assert result == [5, 3, 2, 3, 9, 123, 1]

# Test the function with a list of strings (to include negative decimal values)
test_strings = ["0.5", "1.75", "-1.15", "abc", -6"]
result = get_positive(test_strings)
assert result == [0, 1.5, 1.6]
```