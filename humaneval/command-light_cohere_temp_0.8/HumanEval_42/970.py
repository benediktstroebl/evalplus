```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

#Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    []
]

for item in test_incr_list:
    assert incr_list(item) == [item[1] + 1, item[2] + 1, item[3] + 1]
```