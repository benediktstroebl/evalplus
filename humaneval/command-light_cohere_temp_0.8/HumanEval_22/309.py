Here's a self-contained Python function that filters out integers from a list of mixed data:

```python
def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = ['a', 3.14, 5]
print(filter_integers(values1))  # Output: [5]

values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))  # Output: [1, 2, 3]
```

The function `filter_integers` takes a list of values as input and returns a new list that contains only the integers from the input list. It uses a filter method with the `isinstance` condition to filter out only the integers.

This function is self-contained and can be used to solve the problem of filtering integers from a list of any python values.