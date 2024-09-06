```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -ppi]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ['a', 'b', 'c', 'd', 'e'],
    [1, 2, 4, 6, 8, 9, 10],
]

for test_case in test_cases:
    assert unique(test_case) == [2, 3, 5, 0, 123, 4, 6, 8, 9]
```