```python
def max_element(lst):
    return lst[0] if lst and lst[0] > max(lst[1:]) else max(lst[1:])

# Test cases
tests = [
    [list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])], 123),
    [[]], 0),
    [None], None
]

for case in tests:
    assert max_element(case[0]) == case[1]
```