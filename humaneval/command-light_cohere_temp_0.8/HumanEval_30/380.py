```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = [
    ({' list(-1)': [-1, ], ' list(2): [2, ], ' list([4, 5, 6])': [4, 5, 6, ]},
    ({' list(): [] }, False),
    ({' list([-1, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])': [5, 3, 2, 3, 9, 123, 1]}, True),
]

# Main function
for testcase in test_get_positive:
    assert get_positive(testcase[1]) == testcase[2], f"Test {testcase[0]} failed"
```
This code defines a function `get_positive` that takes a list and returns a new list containing only the positive elements from the original list. It is then tests the the list with a specific structure for passing test cases, including negative or empty lists, as well as lists with positive elements. The code then verifies that the list produced by the `get_positive` function matches the expected output.