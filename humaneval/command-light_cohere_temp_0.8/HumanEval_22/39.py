Here's the self-contained Python function that solves the problem you provided:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values1 = ['a', 3.14, 5]
result1 = filter_integers(test_values1)
assert result1 == [5]

# Test case 2
test_values2 = [1, 2, 3, 'abc', {}, [])
result2 = filter_integers(test_values2)
assert result2 == [1, 2, 3]

# Test case 3
test_values3 = []
result3 = filter_integers(test_values3)
assert result3 == []
```

This function, `filter_integers`, takes a list of values and returns a new list containing only the integers from the input. It uses the simple filtering technique with the `isinstance` condition.