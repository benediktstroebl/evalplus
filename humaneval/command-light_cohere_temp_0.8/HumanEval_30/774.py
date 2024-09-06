```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function
test_get_positive = get_positive

# Test list with negative numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

assert test_get_positive(test_list) == [5, 3, 2, 3, 9, 123, 1]

# Test list with mixed positive and negative numbers
mixed_list = [5, -2, 3, -10, 8, 0, -6]

assert test_get_positive(mixed_list) == [5, -2, 3, -10, 8, 0]
```