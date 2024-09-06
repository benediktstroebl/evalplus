```python
def max_element(lst):
    return max(lst)

# Test cases
test_max_element = [
    [list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123],
    [1, -10],
    [-5, 3, 2, -3, -9, 5]
]

for lst, expected in test_max_element:
    got = max_element(lst)
    assert got == expected, f"Failed for list: {lst}, Expected: {expected}, Got: {got}"
```  This Python code defines a function max_element that calculates and returns the maximum element from a given list. It employs a test cases with lists of numbers and a specific expected maximum value. The code then iterates through the test cases, calls the max_element function on each list, compares the result with the expected maximum, and reports any failures using an informative error message.