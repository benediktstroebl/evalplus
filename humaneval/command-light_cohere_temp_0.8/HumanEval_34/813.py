```python
def unique(l: list):
    return list(set(l))

# Test cases
test_unique = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 7, 5, 2, 'abc', 0, 123, '123'],
    [5, 3, 'three', 5, 0, 1, 2, 'one'],
    ['abc', 'def', 'abc', 'def', 'xyz']
]

for item in test_unique:
    assert unique(item) == set(item), f"Failed for [{!key}] => [{set}] != [{item}]"
```