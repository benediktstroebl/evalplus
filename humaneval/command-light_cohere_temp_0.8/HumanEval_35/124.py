```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with a variety of data
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_max_element([])
test_max_element([5, 9, -7, -6])
test_max_element([2, 8, 7, 6, 5])
```
The function max_element takes a list as input and returns the maximum element in the list using the max() built-in function. This is the the using the quick and efficient way to find the maximum element in a list, it relies on the fact that the maximum element will be at the end of the list.