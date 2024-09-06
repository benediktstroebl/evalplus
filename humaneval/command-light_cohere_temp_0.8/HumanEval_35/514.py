```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = []
test_max_element.add([range(1,10))
test_max_element.add([range(1, 100))
test_max_element.add(range(1, 1000))

for test in test_max_element:
    if max_element(test) != test[0]:
        raise ValueError("Error: Function does not find correct maximum element.")
```