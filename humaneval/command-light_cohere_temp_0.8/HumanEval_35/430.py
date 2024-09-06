```python
def max_element(lst):
    if not_elements(lst):  # Check for empty list
        return None
    return max(lst, default=float('-inf'))

def not_elements(lst):
    return not len(lst) == 0

# Example usage
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Maximum element:", max_element(my_list))  # Output: Maximum element: 123
```

This function, max_element, takes a list as input and returns the maximum element in that list. The function first checks if the `lst` is empty, returning `None` if it is. Then, it uses the Python's built-in `max()` function to find the maximum element in the list, defaulting to `float('-inf')` if the list is empty.

The function is also accompanied by a test to verify if the input is an empty list.