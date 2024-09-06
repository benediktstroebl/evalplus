```python
def unique_digits(x):
    odd = [int(''.join(c for c in s if c % 2 != 0)) for s in x]
    return sorted(odd)
```

The function `unique_digits` takes a list of integers `x` as input and returns a sorted list of all elements that contain no even digits. The function first constructs a list `odd` containing the odd digits found in each integer of the input list, then it sorts the `odd` list in ascending order and returns it.

The code tests include:
```python
# Tests
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
assert unique_digits([152, 323, 1422, 10]) == []
assert unique_digits([52, 32, 4, 74, 62, 811, 111]) == [52, 61, 74, 111]
```