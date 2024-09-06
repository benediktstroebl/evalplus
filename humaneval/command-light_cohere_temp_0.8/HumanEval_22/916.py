Here's a self-contained Python function that filters out integers from a given list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
values_test1 = ['a', 3.14, 5]
print(filter_integers(values_test1))  # Output: [5]

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test2))  # Output: [1, 2, 3]
```

This function, `filter_integers`, takes a list of values as an argument and returns a new list containing only the elements that are integers. It uses the specific type of the input to filter and only returns integers.