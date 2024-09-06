```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
test_get_positive = [
    ('[-1, 2, -4, 5, 6'], [2, 5, 6]),
    ('[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]', [5, 3, 2, 3, 9, 123, 1])
]

def test_function(test_case):
    actual = get_positive(test_case[0])
    expected = test_case[1]
    assert actual == expected, f" unexpectedly returned {actual}, expected {expected}"
    return actual

# Run tests
for test in test_get_positive:
    test_function(test)
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. The test cases section provides a list of test cases, each consisting of a list of values and the expected list of positive numbers. You can add more test cases as needed to verify the correctness of the `get_positive` function.