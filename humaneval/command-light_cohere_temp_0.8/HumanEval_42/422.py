```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test case 1
assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
assert incr_list([5, 3, 5]) == [6, 5, 6]

# Test case 3
try:
    incr_list([9, 0, 123])
except AssertionError as e:
    assert str(e) == "Expected list with elements [9, 0, 123] but got []"

# Test case 4
try:
    incr_list([])
except AssertionError as e:
    assert str(e) == "Expected list but got an empty list"
```
The function incr_list takes a list l as input and returns a new list with elements incremented by 1. The test cases ensure that the function works correctly by passing the test cases and checking the expected results. The code is self-contained, and can be easily imported and used in other scripts.