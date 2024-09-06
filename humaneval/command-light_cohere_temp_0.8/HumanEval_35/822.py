```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test invalid input
# assert max_element([1, 2, 3]) == 3  # this will fail
```  This script defines a max_element function that takes a list lst as input and returns the maximum element in the list. The function uses the using the max function to find the maximum element in the list. The test cases validate the the function.