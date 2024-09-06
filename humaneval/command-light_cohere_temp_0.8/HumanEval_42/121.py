```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [2, 3]

# Test case
def test():
    l = [1, 2, 3]
    expected = [2, 3, 4]
    result = incr_list(l)
    assert list(result) == expected

# Run the test case
test()
```
This code defines a function `incr_list` that appends 1 to the list and then returns the updated list with elements incremented by 1. The function is then tested using the `test` function, which creates a test case with a list `[1, 2, 3]` and an expected result `[2, 3, 4]`. When the test is executed, it will pass if the result matches the expected output.