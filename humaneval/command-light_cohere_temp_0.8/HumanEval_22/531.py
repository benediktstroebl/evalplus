```python
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list of values
test_case_1 = ['a', 3.14, 5]
result_1 = filter_integers(test_case_1)
assert len(result_1) == 3

# Test case 2: Filter integers from a tuple of values
test_case_2 = (1, 2, 3, 'abc', {})
result_2 = filter_integers(test_case_2)
assert len(result_2) == 4

# Test case 3: Filter integers from a list of mixed data
test_case_3 = [1, 2, 3, 'abc', [], 5]
result_3 = filter_integers(test_case_3)
assert len(result_3) == 5
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The script also includes a set of test cases to check the correctness of the `filter_integers` function.