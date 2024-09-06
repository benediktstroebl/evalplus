```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'b', 'c'],
    [None, 'abc']
]

for test_case in test_cases:
    actual = unique(test_case)
    assert actual == [x for x in test_case if x != float('inf')] or
    print(f"Test {test_case} passed.")

```  The test_cases list contains several lists of elements for the unique function to test with. The output will display the test results.