```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1
assertEqual(max_element([1, 2, 3]), 3)

# Test case 2
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]),-123)
```
The function max_element takes a list l as input and returns the maximum element in the list. By using the` max ` function, it will return the maximum value of all elements in the list.

This function is then tested with two different input lists, and the results are compared to the expected maximum element using the assert `function`.