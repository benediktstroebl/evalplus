```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with some examples
list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(list1) == 123

# Test with list of strings
list2 = ["a", "b", "c"]
assert max_element(list2) == "c"

# Test with empty list
list3 = []
assert max_element(list3) == 0
```