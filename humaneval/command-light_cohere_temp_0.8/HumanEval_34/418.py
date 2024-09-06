```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not filtered]

# Test cases
tests = [
    [
        list_factory(),
        [],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [True, False, True],
        [5, 7, 3, 9],
        {5},
    ]
]

for case in tests:
    assert unique(case[0]) == case[1]
```