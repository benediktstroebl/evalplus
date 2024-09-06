```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst, default=float('-inf'))

# Test case 1
print("Max element from the list: ", max_element([1, 2, 3])) # Output: 3

# Test case 2
print("Max element from the list: ", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123

# Test case 3
print("Max element from the list: ", max_element([-5, -3, -13, -100, -200, -1000, -inf, -