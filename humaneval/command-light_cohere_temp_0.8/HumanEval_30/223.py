```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

# Test suite
def test():
    input_list = [-1, 2, -4, 5, 6]
    expected = [2, 5, 6]
    actual = get_positive(input_list)
    assert expected == actual, "Test failed: expected %s but got %s" % (expected, actual)

# Run the tests
test()
```
Do you need anything else?  I hope this helps you with your task.  If was also helpful, I can guide you further if needed.