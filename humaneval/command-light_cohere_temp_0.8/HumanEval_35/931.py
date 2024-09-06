```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
This function will take a list and return the maximum element in that list. It uses the max() function to calculate the maximum element of a list.

The assert statement is used to test the function. It will pass the value to the function and check if the return value is equal to the expected maximum element (123 in this case).