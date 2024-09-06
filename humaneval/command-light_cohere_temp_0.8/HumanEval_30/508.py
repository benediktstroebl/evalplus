```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assert len(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == 7
assert [x for x in get_positive([-100, -200, 0])] == [-200, 0]
```