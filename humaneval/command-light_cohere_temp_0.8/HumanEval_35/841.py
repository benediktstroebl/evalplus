```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various lists and assertions
test_max_element = []
test_max_element.add([1, 2, 3])
test_max_element.add(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10)
test_max_element.add([5, 2, '123', [1, 2, 3, 4, 5])
test_max_element.add(2, 'abc123', [10, 20, 30])

assert max_element(test_max_element) == 123

assert max(test_max_element) == 123

assert len(test_max_element) == 20

try:
    l = [-5, 2, -3, 3, 9]
    assert max_element(l) == 3
    assert len(l) == 5
```