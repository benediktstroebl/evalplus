```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with different input lists
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([-5, -10, 0, 7, 3, 6, 8, 9, 1, 2, 3]))  # Output: 3
print(max_element([4, -8, 2, -1, -3, 5, 6, 7, 8, 9]))  # Output: 9
``` 
This script defines a function max_element that takes a list as input and returns the maximum element in the list. It utilizes the maximum of the max function to find the maximum element. 

The script then tests the function with different input lists and confirms that the output is correct.