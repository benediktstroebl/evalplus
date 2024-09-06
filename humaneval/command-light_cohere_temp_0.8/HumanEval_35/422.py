```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
The provided code defines a function `max_element` that aims to find the maximum element in the input list. It uses the basic Python 'max()' function to achieve this, passing all test cases with different lists and achieving full program correctness.