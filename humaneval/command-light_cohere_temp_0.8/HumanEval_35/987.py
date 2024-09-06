```python
def max_element(lst):
    return max(lst)

# Test the max_element function with some inputs
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
# Test with empty list
assert max_element([]) == None

# Test with list of strings
assert max_element(["Hello", "World!"]) == "World!"

# Test with complex list
assert max_element([1, 2, 3, .5, (10**18)]) == 10**18
```