```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst, default=float('-inf'))

# Test cases
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert max_element([1, 2, 3]) == 3
assert max_element([-5, -3, -10, -20]) == -20
assert max_element([]) == float('-inf')
assert max_element([21, 12, 13]) == 13
```
This code defines a max_element function that calculates and returns the maximum element in the input list lst. It uses the max function with a default argument of negative infinity to handle empty lists, and performs several tests to ensure the correctness of the function with various input scenarios.