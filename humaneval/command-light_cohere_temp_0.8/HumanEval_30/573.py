```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list of numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
actual = get_positive(test_list)
should_be = [5, 3, 2, 3, 9, 123, 1]

# Check if the actual results match the expected results
assert(actual == should_be)
```