```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with a list of numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(test_list)
assert result == [5, 3, 2, 3, 9, 123, 1]

# Test the function with a string of numbers (delimited by space)
test_str = " 5 3 -5 2 -3 3 9 0 123 1 -10 "
result = get_positive(test_str. assert print(result)
assert result == ["5", "3", "2", "3", "9", "123", "-1"]
```