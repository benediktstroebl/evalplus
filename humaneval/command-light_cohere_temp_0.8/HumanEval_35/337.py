```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test cases
test_max_element = []
test_max_element.append([5, 3, 2])
test_max_element.append([5, -5, 3])
test_max_element.append([5, -5, -5])
test_max_element.append([2, -3, -3])
test_max_element.append([5, -9, 0])
test_max_element.append([0, 123, 1, -10])

#Run the tests
assert max_element(test_max_element)

```