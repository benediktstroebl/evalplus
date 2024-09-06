```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with different input
test_list = [1, 2, 3]
test_result = incr_list(test_list)
assert test_result == [2, 3, 4]

test_list2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result2 = incr_list(test_list2)
assert test_result2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The updated Python script defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. The test_function_incr_list function passes the test cases with different lists and asserts the results are correct.