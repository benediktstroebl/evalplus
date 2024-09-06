```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
def test_max_element():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
This script defines a function max_element that calculates the maximum element in the given list. The function passes the proof of correctness using the test_max_element function.