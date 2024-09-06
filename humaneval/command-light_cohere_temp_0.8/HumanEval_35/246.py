```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various lists and expected results
test_max_element = [
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 123
  ]

for test_case, expected_result in test_max_element.pipes test():
    test_case.append(max_element(test_case) == expected_result)
```
This code defines a max_element function that takes a list l as input and returns the maximum element from the list using the max function. The code also includes a list of test cases and uses a loop to iterate through each test case. The function is then called with each test case and the result is compared with the expected result using the == operator.