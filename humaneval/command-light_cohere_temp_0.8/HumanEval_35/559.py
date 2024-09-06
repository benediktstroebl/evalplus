```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test the function with sample inputs
test_max_element = lambda: max_element([1, 2, 3]) == 3
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_max_element()
```
This script defines a function max_element that returns the maximum element in a given list. It also contains a test_max_element, a lambda function that tests the correctness of the max_element function with different inputs.