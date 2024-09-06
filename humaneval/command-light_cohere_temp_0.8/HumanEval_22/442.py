Here is a Python script with a self-contained function that solves the problem of filtering integers from a given list:
```python
# A simple Python function to filter integers from a list
def filter_integers(values):
    return [int(x) for x in values if x.isinstance(int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([4, 2, 'three', 1, 7]))  # []
```

This script provides a function `filter_integers` that takes a list of values and returns a new list containing only the integer values from the input. It uses Python's