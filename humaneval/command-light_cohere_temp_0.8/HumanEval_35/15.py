```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123
print(max_element([]))             # Output: infinity (since empty list has no max)
print(max_element([1, 2, 2, 3, 4, 5])) # Output: 5
```