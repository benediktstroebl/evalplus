```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various lists
test_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_list2 = [-1, 2, -4, 5, 6]
test_list3 = [5, 3, -5, 2, -3, 3, 9, 0, -123]

assert get_positive(test_list1) == [2, 5, 6]
assert get_positive(test_list2) == [2, 5, 6]
assert get_positive(test_list3) == [5, 3, 2, 9]
```
This code defines a function `get_positive` that returns a list containing only the positive elements from an input list `lst`. The function is then tested with various lists using the `assert` statement, which checks if the function's return value matches the expected result.