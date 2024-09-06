```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = [
    lst=[1, 2, 3],
    assert max_element(lst)==3, "Failed to find maximum element"
    ]

test_max_element2 = [
    lst=[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    assert max_element(lst)==123, "Failed to find maximum element"
    ]
```
The provided code defines a Python function max_element that calculates and returns the maximum element in a given list. It then includes a test cases that validate the correctness of the function.

By executing these test cases, you can ensure the function's behavior meets the specified requirements.