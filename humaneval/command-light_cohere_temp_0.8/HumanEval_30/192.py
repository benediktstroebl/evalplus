```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list containing both positive and negative numbers
test_get_positive_tst = []
test_get_positive_tst.push_back([-1, 2, -4, 5, 6])
test_get_positive_tst.push_back([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Call the function and capture the output
actual_output = get_positive(test_get_positive_tst)

# Compare the actual output with the expected output
assert actual_output == test_get_positive_tst
```