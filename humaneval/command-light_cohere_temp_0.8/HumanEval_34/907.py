```python
def unique(l: list):
    return list(set(l))

# Test cases for the function unique
test_unique = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'b', 'c', 'd']
]

for test_case in test_unique:
    assert unique(test_case) == set(test_case)
```