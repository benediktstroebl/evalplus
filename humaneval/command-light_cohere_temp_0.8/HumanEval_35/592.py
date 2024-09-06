```python
def max_element(lst):
    return lst[-1] if len(lst) == 1 else lst[-1] + max(lst[-2:])

# Test cases for the max_element function

assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5]) == 3
assert max_element([-5, -3, -10]) == -10
assert max_element([5, -10, 3, -5]) == -5
assert max_element([5, -10, 3, -3, 3, -5, -100]) == -100
assert max_element([]) == None
```