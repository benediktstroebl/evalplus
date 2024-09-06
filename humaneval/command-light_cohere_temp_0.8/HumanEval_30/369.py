```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function
test_positive = get_positive([-1, 2, -4, 5, 6])
assert test_positive == [2, 5, 6]

# Test handling of negative list
test_negative = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_negative == [3, 2, 1]
```