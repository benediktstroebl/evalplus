```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([5, 3, -5, -20, 2, -3, 3])
assert not get_positive([down_for_tests])

def test_get_positive():
    lst = [-1, 2, -4, 5, 6, 7, -20]
    assert get_positive(lst) == [2, 5, 6, 7]

# Test case with empty list
assert get_positive([]) is True

# Test case with list of strings
lst_strings = ['abc', '', 'abc']
assert get_positive(lst_strings) == []
```
This code defines a function `get_positive` that takes a list as input and returns a new list with only the positive elements from the original list. The test cases verify the the expected behavior of the function for different input scenarios.