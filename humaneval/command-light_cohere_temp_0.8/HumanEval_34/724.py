```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not"]

# Test cases
tests = [
    [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
    # Uncomment to add more large lists or edge cases
    ],
]

for test_case in tests:
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    assert actual == expected, "Failed for test case: " + str(test_case) + ",