```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various input lists

# Test with a list containing only positive numbers
test_positive = [1, 2, 3, 4, 5]
assert get_positive(test_positive) == [1, 2, 3, 4, 5]

# Test with a list containing negative numbers
test_negative = [-1, 2, -4, 5, 6]
assert get_positive(test_negative) == [2, 5, 6]

# Test with a list containing mixed positive and negative numbers
test_mixed = [5, 3, -5, 2, -3, 3, 9, 0, 123, -10]
assert get_positive(test_mixed) == [5, 3, 2, 3, 9, 123]

# Test with empty list
test_empty = []
assert get_positive(test_empty) == []
```

The function `get_positive` takes a list as input and returns a new list containing only the positive numbers from the input. The test cases cover a scenarios, including lists with only positive numbers, lists with negative numbers, lists with mixed positive and negative numbers, and an empty list.