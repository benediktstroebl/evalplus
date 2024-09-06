```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ] ]

# Test cases
test_cases = [
    [],  # [] is not empty
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6],
]

for test_case in test_cases:
    actual_result = unique(test_case)
    expected_result = [0, 2, 3, 5, 9, 123]
    print(f"Test {test_case} - Result: {actual_result}, Expected: {expected_result}")
    print("="end="endl")
```