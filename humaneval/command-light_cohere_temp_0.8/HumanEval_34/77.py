```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

# Test cases
test_cases = [
    [ [5, 3, 5, 2, 3, 3, 9, 0, 123], []],  # Unique([]), Unique([]) => [0, 2, 3, 5, 9, 123]
    [5, 3, 5, 2, 3, 3, 9], [0, 2, 3, 5, 9, 123],  # [5, 3, 5, 2, 3, 3, 9] is not unique
    [5, 3, 5, 2, 3, 3, 9, 0, 1, 2],  # Duplicate values
    ]

for test_case in test_cases:
    assert unique(test_case) == test_case[1:]
 ```