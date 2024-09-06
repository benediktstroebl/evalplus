```python
def max_element(lst):
    return max(lst)

# Test cases
test_max_element = [
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [1, 2, 3, 4, 5],
    [-5, -10, 3, -7, -8, -9]
]

# Function call and results
assert(max_element(test_max_element)) == 123)
for lst, expected in zip(test_max_element, [123, -80]):
    got = max_element(lst)
    assert got == expected, f"Expected {expected}, got {got}"
```  This script defines a function `max_element` that finds and returns the maximum element in a given list. This script also includes a test suite with a variety of test cases. You can use this to ensure your function is working correctly.