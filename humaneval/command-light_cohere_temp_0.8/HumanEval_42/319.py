```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

# Test cases
test_incr_list = [
    (=[1, 2, 3],),
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123 ],),
    ([10, ], [10,]),
]

for test in test_incr_list:
    actual = incr_list(test)
    assert all(map(lambda x: x == test[0][x], actual))
```