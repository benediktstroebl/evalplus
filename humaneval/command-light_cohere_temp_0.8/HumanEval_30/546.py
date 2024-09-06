```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases using the function
test_get_positive = []
test_get_positive.py  # [[-1, 2, -4], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [0, 1, 45, 99, 999]]

# Run the function on test cases and check the results
for test in test_get_positive:
    actual = get_positive(test)
    assert actual == test, f"Error in getting positive numbers: {actual}"
```  # You can uncomment this line to check the test results.

This code defines a function `get_positive` that returns a list containing only the positive numbers from the input list. The test cases are defined to check the correctness of the `get_positive` function.