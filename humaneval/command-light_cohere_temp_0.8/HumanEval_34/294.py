```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [10, 10],
    ['a', 'b', 'c'],
    [(), {}],
    [None, None, 'hello'],
    [1, 2, 3, 4, 5, 6],
]

for case in test_cases:
    assert unique(case) == case
```