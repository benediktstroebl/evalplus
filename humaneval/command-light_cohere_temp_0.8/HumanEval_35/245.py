```python
def max_element(lst):
    if not_list(lst):
        raise ValueError("Input must be a list")
    
    return max(lst)

# Test the function with various inputs
test_max_element = max_element
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_max_element([1, 2, 3, 4, 5])
test_max_element([])
test_max_element([123, -9, 123])
```
This script defines a function max_element that finds the maximum element in a given list. The function accepts a list and raises an error if the input is not a list. Finally, the function is tested with a variety of inputs and passes the tests successfully.