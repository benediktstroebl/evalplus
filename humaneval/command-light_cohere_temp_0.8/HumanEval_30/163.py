```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = [
    ()
    ([-1, 2, -4, 5, 6]),
    ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([100, 101, 102, 103])
]

for test in test_get_positive:
    actual_result = get_positive(test)
    expected_result = test[1]
    assert actual_result == expected_result, f"Test {test}"
```
The provided code defines a function named `get_positive` that takes a list as an argument and returns a new list containing only the positive elements from the original list. The function utilizes a recursive iteration to check if each element in the list is non-negative, and if so, includes it in the resulting list. The test cases section provides a list of test cases, and a loop iterates through each test. The code then executes the test cases, comparing the output of the `get_positive` function with the expected results. If the actual output matches the recent, the test passes, and the function is considered to be correctly implemented.