```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test function to pass the test
def test():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    assert max_element([]) == 0
    assert max_element([True]) == 1
    assert max_element([[-1, 2, 3]]) == 3
```
The code defines a max_element function that finds and returns the maximum element in the list. It also has a test function to test the correctness of the max_element function. The test function verifies the basic cases for lists of different sizes and types, and also for an empty list.