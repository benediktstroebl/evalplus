```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with various inputs
 assert max_element([1, 2, 3]) == 3
 assert max_element([5, 3, -5]) == 3
 assert max_element([-5, -3, -10]) == -10
 assert max_element([5, 0, -5]) == 0
 assert max_element([-10, -3, 123]) == 123
```
The function max_element takes a list lst as input and returns the maximum element in the list using the built-in max() function.