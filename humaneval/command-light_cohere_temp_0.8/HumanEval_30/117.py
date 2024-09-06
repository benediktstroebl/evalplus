```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function
# expected output: [2, 3, 9, 123]
print(get_positive([-1, 2, -4, 5, 6, 7, -9, 0, 123, 1, -10]))

# Test list with mixed values
# expected output: [0, 2, 3, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```