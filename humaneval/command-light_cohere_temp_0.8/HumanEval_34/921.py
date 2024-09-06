```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test cases
test_cases = [
    [
        [],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        ['a', 'a', 'apple', 'asdf'],
        [5, 3, 0, float('inf'), 9, 123],
    ]
)

for test_case in test_cases:
    actual_result = unique(test_case)
    expected_result = [x for x in test_case if x != float('inf')]

    print(f"Test case: {{{ test_case }})\n")
    print(f"Expected result: {{{ expected_result }})\n")
    print(f"Actual result: {{{ actual_result }})\n")
    assert actual_result == expected_result
```