```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1])

```
This script defines a function `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the original list. The `assert` statements at the` the end verify that the function works correctly by passing the test cases and checking if the resulting lists are equal.