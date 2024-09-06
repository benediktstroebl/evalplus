```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases with different lists
print(get_positive([-1, 2, -4, 5, 6]))  # Expected: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected: [5, 3, 2, 3, 9, 123]
print(get_positive([-aha]))  # Error: ValueError: list item 'aha' not in map
```