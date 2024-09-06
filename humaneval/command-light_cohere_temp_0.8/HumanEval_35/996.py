```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = [
    lst=[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    expected=[123]
]

def test():
    assert max_element(test_max_element) == expected

# Run the tests
test()
```