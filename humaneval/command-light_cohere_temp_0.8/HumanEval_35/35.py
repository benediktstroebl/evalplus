```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases for the function
test_max_element = [
    [1, 2, 3],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

for case in test_max_element:
    assert max_element(case) == max(case), f"Failed for case: {case}"
```