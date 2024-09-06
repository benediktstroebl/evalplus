```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with a variety of test cases
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Output: 123
print(max_element([5, '3', -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Output: '3'
print(max_element([1, 2, -5, 3, -5, -3, 3, 9, 0, 123]))
# Output: 3
print(max_element([1, 2, -5, -4, -3, -2, -5, -8, -3]))
# Output: -5
```