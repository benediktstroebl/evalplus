Here is a self-contained Python function that filters integers from a given list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list
test_case_1 = ['a', 3.14, 5]
result_test_case_1 = filter_integers(test_case_1)
assert result_test_case_1 == [5], "Test case 1 failed: Got %s instead of [5]"

# Test case 2: Filter integers from a list with non-integer elements
test_case_2 = [1, 2, 3, 'abc', {}, []]
result_test_case_2 = filter_integers(test_case_2)
assert result_test_case_2 == [1, 2, 3], "Test case 2 failed: Got %s instead of [1, 2, 3]"
```

The function `filter_integers` uses the Python `isinstance` function to check if each element in the input list is an integer. The function returns a filter result as a list of integers from the input list.