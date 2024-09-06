```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x+1 for x in l]

# Test cases
test_incr_list = [
    [
        (1, [1]),
        (2, [2, 3]),
        (3, [5, 3, 3])
        (4, [])
        (5, [5, 2, 3])
    ], 
    (['\n'], [1, 2, 3])
]

def test_function(test_case):
    """
    actual = [x+1 for x in test_case[0]]
    expected = test_case[1]
    assert actual == expected, f"AssertionError: {actual} != {expected}"

test_incr_list = test_function(test_incr_list)
```