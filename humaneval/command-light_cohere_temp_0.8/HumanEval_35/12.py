```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 2
assert max_element([1, 2, 3, 4, 5]) == 5

# Test case 3
assert max_element([-5, -3, -10, -8, -4, -2, -6, -1, -100]) == -100
```
The function max_element in this code accepts a list lst as input and outputs the list's maximum element. The test cases that function's behavior is then validated using assert statements.