```python
def max_element(lst):
    return max(lst)

# Test the max_element function with various lists
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]) == 123
assert max_element([5, 3, -5, 2, -3]) == -5
assert max_element([-10, -5, -20]) == -20
```
The code defines a function max_element that takes a list lst as input and returns the maximum element in the list. It uses the maximum selector to find the maximum element. This function is also be tested successfully with various input lists.