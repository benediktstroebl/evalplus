```python
def unique_digits(x):
    # Sort list of positive integers without any even digit
    return sorted([i for i in x if i % 10 != 0])

# Test cases
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
assert unique_digits([152, 323, 1422, 10]) == []
assert not unique_digits([161, 323, 1422, 10])
```