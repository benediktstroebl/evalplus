```python
def unique(l: list):
    return list(set(l))

# Test cases
test_unique = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 5, 7, 2, 6, 1],
    ['a', 'b', 'c'],
    [0, 2, 3, 0, 0, 1, 3, 4, 2],
]

for test_case in test_unique:
    assert unique(test_case) == test_case[1:]
```