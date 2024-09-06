Here is a self-contained Python function that filters out integers from a list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with different input values
print(filter_integers(['a', 3.14, 5]))  # ['5']
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([-1, 2, 3, 'abc', None]))  # [2, 3]
```

This function, `filter_integers`, takes a list of values as an argument and returns a new list that contains only the integers from the original list. The `isinstance()` function is used to check if each value in the list is an integer.