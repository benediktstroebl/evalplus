```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print(filter_integers(values1))  # Output: [5]
print(filter_integers(values2))  # Output: [1, 2, 3]
```

This code defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses a Python's `isinstance` function to check if each value is an integer. 

Test cases are defined with two lists of different types of values. The function is then called with both test lists and the output is printed to the console to verify the results.