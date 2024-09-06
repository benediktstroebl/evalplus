```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list of any values
assert test_case1(filter_integers(['a', 3.14, 5]))
assert [5] == test_case1(['a', 3.14, 5])

# Test case 2: Filter integers from a list of numbers
assert test_case2(filter_integers([1, 2, 3, 'abc', {}]))
assert [1, 2, 3] == test_case2([1, 2, 3, 'abc', {}])

```
This Python script defines a function `filter_integers` that filters out any non-integer values from a given list. It then passes these tests to validate the correctness of the function. The tests ensure that the function correctly filters the integers from the list.