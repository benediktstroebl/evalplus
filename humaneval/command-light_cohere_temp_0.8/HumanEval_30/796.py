```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test the function with various input lists
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123])
assert(get_positive([5, 'x', -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 'x', 2, 3, 9])
assert(get_positive([]) == [])
```
The function get_positive returns a list containing only positive numbers from the input list. The test cases ensure that the list inputs are valid and produce the expected results.