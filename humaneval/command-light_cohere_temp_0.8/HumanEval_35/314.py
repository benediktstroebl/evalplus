```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = []
test_max_element.add([range(1, 10, 1), [1, 2, 3, -5, -3, -4, 0, 5, 6, 7, 8, 9])
test_max_element.add([range(1, 20, 1), [1, -5, 3, -200, 200, 5, 8, 3, -1, -300, 300])

# Main program
test_max_element = all(test_max_element)
assert max_element(test_max_element) == 9

print("All tests passed!")
```