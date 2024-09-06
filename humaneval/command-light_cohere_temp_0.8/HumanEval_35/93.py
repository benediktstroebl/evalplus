```python
def max_element(lst):
    return lst[-1] if len(lst) == 1 else max(lst)

# Test cases
assertEqual(max_element([1, 2, 3]) , 3)
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) , 123)
``` 
This script defines a function `max_element` that returns the maximum element in the list. It achieves this by returning the max element if the list has only one element, and uses the `max()` function to return the maximum element otherwise. 

The test cases validate that the function works correctly for various lists.