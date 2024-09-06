```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n + 1): result[i] = l[i - 1] + 1
    return result

# Test the function
def test_incr_list():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    for item, expected_item in zip(lst, expected):
        assert item == expected_item, f"Did not get expected item: {item} != {expected_item}"
    print("All tests passed!")
test_incr_list()
```
This Python script defines a function `incr_list` that increases the list elements by 1 and tests the function using a `test_incr_list` function that checks if the output matches the expected result.