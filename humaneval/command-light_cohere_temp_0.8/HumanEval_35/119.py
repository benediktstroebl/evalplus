```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test function
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
The provided code defines a Python function `max_element` that calculates and returns the maximum element from the input list `l`. The function uses the Python built-in `max()` function to achieve this. The test_max_element function verifies the correctness of the `max_element` function by passing different lists with known maximum elements (in this case, [1, 2, 3] and [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) and expecting the correct result. 
The `max_element` function passes all the test cases successfully.