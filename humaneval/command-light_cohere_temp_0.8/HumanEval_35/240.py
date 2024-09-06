```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
print("Maximum element in the list:", max_element([1, 2, 3]))  # Output: 3

# Test case 2
print("Maximum element in the list:", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123

# Test case 3
print("Maximum element in the list:", max_element([5, -5, 3, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```
This script defines a function max_element that computes and returns the maximum element in a given list. The script then tests the maximum element on three different lists, and the output is the value of the maximum element from each test case.