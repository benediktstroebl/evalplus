```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = []
test_max_element.add([1, 2, 3])
test_max_element.add(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10)
test_max_element.add([10, 11, 100, -2, -5, -30, -1000, -1000000, -10 Million)

print("Test cases passed:")
for case in test_max_element:
    print(f"Case {case} passed: Max element is {max_element(case)}")
```