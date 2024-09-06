```python
def unique(l: list):
    return list(set(l))

# Test cases for unique function
unique_test = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 7, 2, 6, 1, 4, 5, 3],
    ['a', 'e', 'f', 'A', 'B', 'T', 'F'],
    [[]],
]

for test_set in unique_test:
    actual_set = set(test_set)
    expected = set(unique(test_set))
    print(f"Test 1: {actual_set}, {expected}")
    assert actual_set == expected
```