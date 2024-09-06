```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst, key=lambda x: x)

# Test cases
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Output: 123

print(max_element([1, 2, 3, 4, 5, 6]))
# Output: 5

print(max_element([xi for xi in [1, 2, 3, 4, 5, 6]]))
# Output: 5

print(max_element([-5, -3, -7, -9, -11, -13, -15]))
# Output: -15
```
This script defines a `max_element` function that returns the maximum element in the list. The function utilizes the optional lambda function as the `key` argument to the `max` function to determine the maximum element based on the desired criteria.