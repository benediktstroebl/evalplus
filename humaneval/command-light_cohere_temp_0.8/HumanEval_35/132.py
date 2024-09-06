```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
# Test edge cases
assert max_element([]) == None
assert max_element([1, 2, 3]) == 3
assert max_element([10, -10]) == -10
assert max_element([[-10, -20]) == [-20])
```
The function max_element takes a list as an argument and returns the maximum element in the list. This function is optimized by using the built-in max() function, which avoids unnecessary creation of a new list.