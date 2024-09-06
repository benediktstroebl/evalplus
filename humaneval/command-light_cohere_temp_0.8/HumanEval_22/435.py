```python
def filter_integers(values):
    return [num for num in values if isinstance(num, int)]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert isinstance(result1, list), "The result should be a list"
assert len(result1) == 3, "The result should have 3 elements"
assert all(isinstance(x, int) for x in result1), "The result should only contain integers"

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert isinstance(result2, list), "The result should be a list"
assert len(result2) == 4, "The result should have 4 elements"
assert all(isinstance(x, int) for x in result2), "The result should only contain integers"

# Test case 3
values3 = [1, 2, 3, 'abc', {}]
result3 = filter_integers(values3)
assert isinstance(result3, list), "The result should be a list"
assert len(result3) == 3, "The result should have 3 elements"
assert all(isinstance(x, int) for x in result3), "The result should only contain integers"
```

This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. This function is testing that a list of strings, integers, and a dictionary, successfully filtering out the integers from the input.