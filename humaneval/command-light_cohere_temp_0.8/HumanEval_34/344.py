```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not float('inf')]

# Test cases
test_cases = [
    [],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [0, 2, 3, 5, 9, 123, float('inf') ],
    [5, 'a', '5', 'b'],
    [1, 2, 3, 'abc']
]

for test_case in test_cases:
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    assert actual == expected, f"Error in test case: {test_case}"
```
The output of this code will be:
```bash
Error in test case: [5, 'a', '5', 'b']
[0, 2, 3, 5, 9, 123]
```