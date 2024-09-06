```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l[:] = [x + 1 for x in l]
    return l

# Test case
test_incr = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_incr_result = incr_list(test_incr)
print(test_incr_result)

# Correct increment
test_correct = [1, 2, 3, 4]
test_correct_result = [x + 1 for x in test_correct]
print(test_correct_result)
```
This function 'incr_list' takes a list as an argument and returns a new list with elements incremented by 1. The test cases ensure the example and the expected output is printed.

Note: The function and tests are self-contained, meaning they are completely written in the provided Python script and do not require any external inputs or dependencies.