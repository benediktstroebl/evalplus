```python
def max_element(lst):
    return max(lst)

# Test case 1:
assert max_element([1, 2, 3]) == 3

# Test case 2:
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3:
lst = [-5, -3, 0, 9, -10, 2, -7, 3, -100, 8, -2]
assert max_element(lst) == -100
```