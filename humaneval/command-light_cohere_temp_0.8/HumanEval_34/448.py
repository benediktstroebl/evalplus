```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test cases
test_cases = [
    [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        ['abc'],
        ['a', 'a'],
        [1, 2, 3, 4, 5],
    ]
]

for test_case in test_cases:
    actual_result = unique(test_case)
    expected_result = [0, 2, 3, 5, 9, 123]
    assert actual_result == expected_result, f"Test case {test_case} failed: {actual_result}"
```

This code defines a function called unique that returns a list of unique elements from a given list. It uses a same set to track the elements seen so far and creates a new list containing only the unique elements. The test cases section includes a list of test cases, each containing a list of values and an expected unique list. The code then iterates through each test case, calls the unique function with the test case, and asserts that the actual result is equal to the expected unique list.