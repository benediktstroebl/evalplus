Here's a self-contained Python function that filters out integers from a list of any python values:
```python
def filter_integers(values):
    """
    Filter given list of any python values and return only integers
    :param values: list of any python value
    :return: list of int
    """
    return [x for x in values if isinstance(x, int)]

# Test the function
values_test = [1, 'a', 3.14, 5]
result_test = filter_integers(values_test)
print(result_test) # Output: [1, 3.
```

The function takes a list of values and returns a new list with only the integers from the original list. This is a way to use the function to filter out integers from a list of any values.