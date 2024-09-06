```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Basic test cases
print("Maximum element:", max_element([1, 2, 3]))  # Output: 3
print("Maximum element:", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123

# Edge case: empty list
print("Maximum element:", max_element([]))

# Edge case: single element list
print("Maximum element:", max_element([1]))
```

This code provides a function max_element that simply returns the maximum element from the passed list. The test cases verify the correct behavior of the function with various inputs. The edge cases for empty list and single element list also are covered.