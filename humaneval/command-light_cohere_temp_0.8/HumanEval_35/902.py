```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = [
    [1, 2, 3],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [-5, 3, -2, 101, 102, 103],
]

for lst, want in test_max_element:
    got = max_element(lst)
    assert got == want, f"Failed for {lst}, expected {want}, got {got}"
```
The test cases provided are a list of lists, each containing a list of numbers and the desired maximum element. The code defines a test_max_element list with the test cases and then loops through each test case, calling the max_element function and comparing the result with the expected maximum element from the corresponding list.