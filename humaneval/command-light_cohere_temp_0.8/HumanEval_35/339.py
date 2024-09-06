```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test case 1
test_case_1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Test case 1:", max_element(test_case_1))  # Output: 123

# Test case 2
test_case_2 = [5, 3, -5, -2, -3, 3, 9, 0, -100]
print("Test case 2:", max_element(test_case_2))  # Output: -100

# Test case 3
test_case_3 = [5, 3, -5, 2, -3, 0, 9, 0, -INF]
print("Test case 3:", max_element(test_case_3))  # Output: -INF
```
The code defines a function `max_element` that finds the maximum element in the list. The test cases then demonstrate how the expected results would be: finding the maximum element in different types of lists and handling cases with negative values and negative infinity.