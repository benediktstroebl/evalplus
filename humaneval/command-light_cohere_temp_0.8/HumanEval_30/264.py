```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test cases for get_positive function

# Test case with a list of all positive numbers
test_positive_list = [1, 2, 3, 4, 5]
assert get_positive(test_positive_list) == [1, 2, 3, 4, 5]

# Test case with list of all negative numbers
test_negative_list = [-1, -2, -3, -4, -5]
assert get_positive(test_negative_list) == []

# Test case with a list of mixed positive and negative numbers
test_mixed_list = [5, -3, 2, -4, 0]
assert get_positive(test_mixed_list) == [5, -3, 2, 0]

# Test case with a list of numbers greater than or equal to 0
test_positive_greater = [0, 1, 2, 3, 4, 5]
assert get_positive(test_positive_greater) == test_positive_greater

# Test case with a list of numbers less than 0
test_negative_less = [-6, -7, -8]
assert get_positive(test_negative_less) == []
```
The `get_positive` function filters out and returns only the positive numbers from the input list. 
This script provides comprehensive test cases to validate the correctness of the `get_positive` function. 
It covers various scenarios, including positive, negative, mixed numbers, and numbers greater than 0, and verifies that the function returns the expected results.