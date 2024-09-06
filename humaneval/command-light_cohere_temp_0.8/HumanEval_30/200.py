```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with various input lists
test_get_positive = []
test_get_positive.py  # - [[-1, 2, -4], [5, 3, -5, 2, -3, 3, 9, 0, 123], [-10]]

# Verify the output
assert list(get_positive(test_get_positive)) == test_get_positive  # [2, 3, 2, 3, 9, 123]
```