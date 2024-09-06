```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test cases
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]) == 123
assert max_element([]) == None
assert max_element([5, -5, 5, -10, -5]) == -5
```
The function max_element takes a list as input and uses the built-in max() function to return the maximum element in the list.