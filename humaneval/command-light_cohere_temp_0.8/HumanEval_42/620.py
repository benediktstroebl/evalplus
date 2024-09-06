```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.append(l[n] + 1)
    return l

# Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [10, 11, 12],
]

for item in test_incr_list:
    actual = incr_list(item)
    assert actual == [1, 3, 5, 4, 7, 10], "Incorrect result"
```
This script defines a function `incr_list` that returns a new list with elements incremented by 1. The test cases ensure that the function produces the expected results for different input lists.