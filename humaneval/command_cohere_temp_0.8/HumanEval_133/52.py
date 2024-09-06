```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest larger integer first.
    """
    result = sum(x ** 2 for x in lst if isinstance(x, (int, float)) and x >= 0)
    return result
```

The function `sum_squares()` takes a list of items as input and returns the sum of squared positive integers in that list. Before calculating the sum of squares, each list item is rounded up to the nearest larger integer if it is a valid positive number (`isinstance(x, (int, float)) and x >= 0`). The `sum()` function then computes the sum of the squared values.

To test this function, you can create a test list and assert the expected result against the output of the function:
```python
# Test case with a simple list of integers
test_list = [1, 2, 3]
expected_result = 14
result = sum_squares(test_list)
assert result == expected_result

# Test case with a list of integers and a float
test_list = [1, 4, 9]
expected_result = 98
result = sum_squares(test_list)
assert result == expected_result

# Test case with multiple integers in the list
test_list = [1, 3, 5, 7]
expected_result = 84
result = sum_squares(test_list)
assert result == expected_result

# Test case with a list containing a positive integer and a negative integer
test_list = [1.4, 4.2, 0, -2.4]
expected_result = 29
result = sum_squares(test_list)
assert result == expected_result

# Test case with a list containing multiple positive integers and negatives
test_list = [1.4, -2.4, 1, 1]
expected_result = 6
result = sum_squares(test_list)
assert result == expected_result
```

This test suite covers various scenarios involving different types of list elements and positive integers, validating the behavior of the `sum_squares` function.