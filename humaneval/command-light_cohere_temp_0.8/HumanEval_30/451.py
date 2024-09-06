```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test suite with specified inputs and expected outputs
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]

# Main code to execute the function and run the tests
get_positive([-1, 2, -4, 5, 6])
test_get_positive()
```