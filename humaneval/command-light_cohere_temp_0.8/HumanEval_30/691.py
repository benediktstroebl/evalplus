```python
def get_positive(input_list):
    """Return only positive numbers in the list"""
    return [num for num in input_list if num > 0]

# Test the function with different input lists 

# [get_positive([-1, 2, -4, 5, 6])] # Output: [2, 5, 6]
# [get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])] # Output: [5, 3, 2, 3, 9, 123, 1]
```
This function will take a list and will return a new list with all the positive numbers.