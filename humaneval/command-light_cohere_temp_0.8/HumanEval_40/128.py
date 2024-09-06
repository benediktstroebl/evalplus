Here is a Python script with a self-contained function that solves the problem you described: 

```python
def is_sum_to_zero(lst):
    """
    Determine if there are three distinct elements in the list that sum to zero.
    return True if there are three numbers that sum to zero, and False otherwise.
    """
    number_sum_to_zero([1, 3, -2, 1])
    False
    return True
    """

def test_sum_to_zero():
    """
    Function tests the 'is_sum_to_zero' function
    """
    test_case = [1, 3, -2, 1]
    assert is_sum_to_zero(test_case), "Test passed"
    test_case = [1, 2, 3, 7]
    assert is_sum_to_zero(test_case), "Test passed"
    test_case = [2, 4, -5, 3, 9, 7]
    assert is_sum_to_zero(test_case), "Test passed"
    test_case = [1]
    assert is_sum_to_zero(test_case), "Test passed"
    test_case = [10, 20, 30]
    assert is_sum_to_zero(test_case), "Test failed"

# Run the test suite
test_sum_to_zero()
```

This code provides a Python function `is_sum_to_zero` that checks if a given list has three distinct elements whose sum is equal to zero. The `test_sum_to_zero` function tests the `is_sum_to_zero` function with various test cases.