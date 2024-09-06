```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 2
assert max_element([2, 3, -10, 0]) == 3

# Test case 3
assert max_element([1, 2, 3, -5, -6, -10]) == -5

# Test case 4
assert max_element([-5, 3, -10, -20, -30, -40, -60, -70, -80, -90]) == -80

# Test case 5 (invalid input)
assert max_element([1, 2, 3]) is None
```