```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function with various lists
for test_list in [[5, 3, -5], [2, 4, 6], [1, 9, 3, 7], [0, 123, 1, 2, -10]]:
    result = max_element(test_list)
    assert result == max(test_list)  # Pass test
```