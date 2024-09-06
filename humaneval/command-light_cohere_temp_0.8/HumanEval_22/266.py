```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case: Filter integers from a list
test_values = [1, 2, 3, 'abc', {}, [5])
result = filter_integers(test_values)
assert len(result) == 4, "The length of the result should be 4"
assert all(isinstance(x, int) for x in result), "The result should only contain integers"

# Test case: Filter integers from a tuple
test_tup = (1, 2, 3, 'abc', [], 5)
result_tup = filter_integers(test_tup)
assert len(result_tup) == 5, "The length of the result should be 5"
assert all(isinstance(x, int) for x in result_tup), "The result should only contain integers"

# Test case: Filter integers from an iterable
test_iterable = [1, 2, 3, 4, 5]
result_iter = filter_integers(test_iterable)
assert len(result_iter) == 5, "The length of the result should be 5"
assert all(isinstance(x, int) for x in result_iter), "The result should only contain integers"
```

This script defines a function **filter_integers** that accepts a list of values and returns a new list containing only the integers from that input. The test cases provided afterwards demonstrate the testing the function by passing different types of input and verifying that the output is as expected.