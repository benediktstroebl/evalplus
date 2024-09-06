```python
def max_element(lst):
    if not_list(lst):  # Check if list is valid
        raise TypeError("Input must be a list")
    return max(lst)

# Test the function with a variety of inputs
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_max_element([1, 2, 3])
test_max_element([-5, -3, 7, -9])
test_max_element([1, 2, 3, -7, -5, -3])
```
The above Python code defines a function `max_element` that finds the maximum element in a given list. It employs some input validation to ensure the list is valid and raises a `TypeError` if it's not. 

This function can then be used to find the maximum element in various types of lists.