```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Basic test case using list comprehension
print("max element:", max_element([1, 2, 3]))  # Output: 3

# Test case with negative numbers
print("max element:", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, -10]))  # Output: 123

# Test case with complex numbers
print("max element:", max_element([9, 0, 123, 1, -10]))  # Output: 123

# Test case with mixed integers and floats
print("max element:", max_element([5.0, 3, 2, -3.5, 4.5]))  # Output: None
```