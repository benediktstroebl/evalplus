```python
def max_element(lst):
    return lst[0] if lst and lst[0] >= all(lst[1:]) else lst[-1]

# Test cases:
test_max_element = []
test_max_element.add([1, 2, 3])
test_max_element.add([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_max_element.add([5, -5, 0, 0, 1, -20, 'abc'])

# Assertions:
for test in test_max_element:
    assert max_element(test) == test[0], f"Expected: {test[0]}, Actual: {max_element(test)}"
```  I hope this helps! Please feel free to ask any further questions!