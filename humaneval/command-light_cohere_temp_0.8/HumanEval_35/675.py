```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = []
test_max_element.add([1, 2, 3])
test_max_element.add(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10)

assert max_element(test_max_element) == 3

test_max_element.add([5, [1, 2, 3])
test_max_element.add([5, [1, 2, 3, [4, 5, 6]])

assert max_element(test_max_element) == 5

test_max_element.add([5, [1, 2, 3, -20])
test_max_element.add([5, [20, [1, 2, 3], 4])

assert max_element(test_max_element) == 5

test_max_element.add([5, [-20, -100])
test_max_element.add([5, [-10, -100, -20])

assert max_element(test_max_element) == -100

```