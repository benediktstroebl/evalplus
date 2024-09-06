```python
def max_element(lst):
    return lst[0] if lst and max(lst) else lst[0]

# Test cases for max_element function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert max_element([1]) == 1
assert max_element([]) == float('inf')
assert max_element([2, -2, -4]) == float('-inf')
assert max_element([1, 2, -3]) == 2
```