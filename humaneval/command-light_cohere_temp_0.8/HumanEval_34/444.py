```python
def unique(l: list):
    seen = set()
    return [x for x in l if x not in seen and not in [0, ] ]

# Test cases
tests = [
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123], ),
    ([12, 7, 8, 1, 4, 2],),
    ([],),
]

for test_case in tests:
    actual = unique(test_case)
    assert set(actual) == set(test_case), "Test case failed: " + str(test_case) + " should be unique"
```