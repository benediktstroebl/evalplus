```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [1, 2, 3, 'abc', {}, [5, 6])
result = filter_integers(values)
assert len(result) == 6  # Assertion to verify the output length
assert all(isinstance(x, int) for x in result)  # Assertion to verify the output is integers
```

This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses a value of `isinstance` to filter out any non-integer values.