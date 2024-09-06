```python
def unique(l: list):
    return sorted(set(l))

# Test cases
test_unique = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'b', 'c'],
    ['1', '2', '3', '4', '5'],
    [5, '123', '5']
]

for test_case in test_unique:
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    assert actual == expected, f"Failed in test case: {expected}, {actual}"
```
The function `unique` returns a sorted set of unique elements in the input list. This ensures all elements are unique, and we can get the sorted list back.