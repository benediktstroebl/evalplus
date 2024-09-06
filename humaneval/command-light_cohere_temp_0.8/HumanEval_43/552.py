```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test the test cases, which should succeed, are included in the function.
# Example a list of integers [1, 2, 3, 7]
result = pairs_sum_to_zero([1, 2, 3, 7])
assert result == True

# Example list of integers
test_list = [1, 2, 3, 0, 7]
result = pairs_sum_to_zero(test_list)
assert result == True

# List with two elements that sum to zero
test_list = [0, 2]
result = pairs_sum_to_zero(test_list)
assert result == True

# List with two elements that do not sum to zero
test_list = [1, 3]
result = pairs_sum_to_zero(test_list)
assert result == False
```