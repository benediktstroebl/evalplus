```python
def max_element(lst):
    return lst[0] if lst and lst[0] > max(lst[1:]) else max(lst[1:])

# Test cases
tests = [
    [list([1, 2, 3]), max_element(list)], 3),
    [list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) ,max_element(list)], 123),
    [list(), max_element(list)], None,
    [-100, -100, -100], max_element([])], -100
]

for test_case in tests:
    assert max_element(test_case[0]) == test_case[1]
```