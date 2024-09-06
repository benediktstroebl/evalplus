```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Basic test cases
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([]))        # Output: None
print(max_element([1, 2, 3, 4, 5])) # Output: 5

# Edge case: Empty list
print(max_element([]))        # Output: None

# Edge case: Single element list
print(max_element([9]))        # Output: 9
```
The function max_element takes an input list lst and returns the maximum element in the list. The function is self-contained and uses the built-in max() function to return the maximum element. The test cases cover a following: basic, edge cases, and single element case.