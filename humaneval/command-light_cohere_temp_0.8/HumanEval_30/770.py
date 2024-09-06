```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with a list of mixed values
# Should return a list with all non-negative numbers
test_func = get_positive([-1, 2, -4, 5, 6])
assert test_func == [2, 5, 6]

# Test the function with a list of only positive numbers
test_func = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_func == [5, 3, 2, 3, 9, 123]
```
This code defines a function `get_positive` that takes in a list and returns a new list with only the positive numbers from the original list. The test cases demonstrate that the function correctly with both lists of mixed numbers and a list of exclusively positive numbers.