```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [6, 7, 8, 9]
]

for test_case in test_incr_list:
    actual = incr_list(test_case)
    assert all(map(lambda x: x == test_case[x], actual)))
```