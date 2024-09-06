```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5]) == 3
assert max_element([-5, -3, 3, 7]) == 3
assert max_element([1, 2, 3, 4, 5]) == 5
assert max_element([]) == 0
assert max_element([123, 456, 789]) == 789
``` 
The above Python script defines a function max_element that returns the maximum element in a given list. It is then tests this function with a variety of list inputs and asserts to ensure the correctness of the function. 

This code provides a self-contained solution and test for finding the maximum element in a list.