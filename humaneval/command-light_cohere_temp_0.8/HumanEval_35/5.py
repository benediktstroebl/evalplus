```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various input lists
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123
print(max_element([-5, -3, -10, -100, 2, 5, -20, 1])) # Output: -100
print(max_element([123, 2, 3, -22, 11, 7, 8, 22, -33])) # Output: 11
print(max_element([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 9
```