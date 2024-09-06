```python
def max_element(lst):
    return max(lst)

# Test cases
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case with list of strings
assert max_element(['A', 'B', 'C']) == 'B'

# Test case with empty list
assert max_element([]) == None

# Test case with list of negative numbers
assert max_element([-5, -10, -3, -2, -1]) == -1
```

The provided code has a function `max_element` that finds the maximum element in a given list. The test cases after the also cover scenarios with positive numbers, negative numbers, empty lists, and strings. Furthermore, it checks if the maximum element of strings is indeed the first character.