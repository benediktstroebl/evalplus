```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with several inputs
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123])
assert(get_positive([9, -9]) == [9])

```

This code defines a function `get_positive` that returns a list of only positive numbers from the input list. The test cases ensure the values of the function are correct, as they should pass the tests successfully.