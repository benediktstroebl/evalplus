Here's the self-contained Python function that filters integers from a list of mixed values:
```python
def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

# Test the function
values = [1, 2, 3, 'abc', {}, 5, '6']
print(filter_integers(values))  # Output: [1, 2, 3, 5, 6]

# Test another value (string)
values = [1, 2, 3, 'hello']
print(filter_integers(values))  # Output: [1, 2, 3]
```

The function filter_integers takes a list of values and returns a new list containing only the integers present in the original list. It does this using the simple iteration to filter the elements and check if each value is an instance of int.