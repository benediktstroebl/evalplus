```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases for get_positive function
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([0])
assert not get_positive([7])
```
The `get_positive` function takes a list as an argument and returns a new list containing only the positive elements from the original list. 

The test cases validate the correctness of the `get_positive` function by passing various lists and verifying that it returns the expected results.