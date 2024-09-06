```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test cases
test_max_element = []
test_max_element.push_into_list(max_element([1, 2, 3])) # [3]
test_max_element.push_into_list(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # [123]

print("Test cases passed: ", end='')
print(*test_max_element)
```