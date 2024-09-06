```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test suite
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Main script execution
test_get_positive()
``` 
This Python script defines a function `get_positive` that filters out negative numbers from an input list, and tests the function with several input lists to ensure it's correctness.  The test_get_positive function is then called to run the test suite and verify the results.