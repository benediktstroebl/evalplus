```python
def max_element(lst):
    return lst[-1] if len(lst) == 1 else max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

```

This function `max_element` takes a list `lst` as an argument and uses the list's last element to solve the problem in case of a single-element list, and the `max()` function to solve the problem in case of a list with more than one element.