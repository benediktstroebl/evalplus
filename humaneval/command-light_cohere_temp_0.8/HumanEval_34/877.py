```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [10, 20, 30, 40, 50],
    [23, 34, 35, 45, 56, 67, 78],
]

for test_case in test_cases:
    print("Test:", test_case)
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    assert actual == expected, f"Unexpected result: {actual}"
```
This script defines a function `unique` that returns a list with unique elements from the input list, and the test cases pass various lists to this function and verify the expected results. 
The use of assert statements to check the outputs against the expected values, ensuring that the function is working correctly.