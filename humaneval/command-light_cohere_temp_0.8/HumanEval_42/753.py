```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [i+1 for i in l] + l
    return res

# Test the function with various input
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert list(incr_list(test_list)) == [6, 3, 6, 4, 6, 4, 4, 10, 1, 124], "Test passed"

test_one_item = [1]
test_two_items = [5, 3]
assert incr_list(test_one_item) == [1, 2], "Test failed with one item"
assert incr_list(test_two_items) == [6, 3], "Test failed with multiple items"

test_empty_list = []
assert incr_list(test_empty_list) == [], "Test passed with empty list"
```