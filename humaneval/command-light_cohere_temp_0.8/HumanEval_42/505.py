```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2, 3] + l

# Test cases
test_incr_list = [
    ()
    [1, 2, 3]
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
]

for test in test_incr_list:
    print(f'Test {test}')
    actual = incr_list(test)
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert actual == expected
```