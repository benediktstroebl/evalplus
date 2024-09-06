```python
def max_element(lst):
    if not_elements(lst):  # Empty list
        return None
    return max(lst, key=lambda x: x)

def test_max_element():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
This code defines a function max_element that returns the maximum element in a list, based on a custom comparison key lambda function. The test_max_element function verifies that max_element correctly identifies the maximum element in the provided list.