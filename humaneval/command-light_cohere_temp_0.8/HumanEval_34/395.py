```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test cases
tests = [
    (
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        "Should return list with duplicates removed and sorted",
        ["0", "2", "3", "5", "9", "123"],
    ),
    (
        [],
        "Should return empty list",
        [],
    ),
    (
        ["5", "3", "5", "2", "3", "9", 0, 123],
        "Should keep only unique elements",
        ["0", "2", "3", "5", "9", 123],
    ),
]

for case, test_description, expected in tests:
    actual = unique(case)
    print(f"Case {case}: {test_description}")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    assert actual == expected
```