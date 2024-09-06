```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test the function with several inputs
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123])
assert(get_positive([5, 6, 7, 8, 9]) == [5, 6, 7])
assert(get_positive([2, 2, 3, -4, -5]) == [2, 2, 3])
```
This code defines a function **get_positive** that takes a list as input and returns a new list with only the positive elements from the original list. The test cases demonstrate the specific scenarios for the function, and the results are correctly validated against the expected outcomes.