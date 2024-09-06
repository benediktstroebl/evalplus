```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2, 3]

#Test cases
test_incr_list = [
    [
        (True, [1, 2, 3]),
        (False, [5, 3, 5, 2, 3, 3, 9, 0, 123])
    ]
)

#Execute the tests
for test, expect in test_incr_list:
    assert incr_list(test) == expect
```