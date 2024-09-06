```python
def max_element(lst):
    return max(lst)

# Test the max_element function with various lists
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert max_element([-5, -3, -10]) == -10
assert max_element([]) == float('-inf')
assert max_element([123, 45, 67, 89]) == 89
```