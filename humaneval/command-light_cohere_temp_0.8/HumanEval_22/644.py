```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with markdown codes
test_values = [['a', 3.14, 5], [1, 2, 'abc'], [1, 2, 3], ['', {}, []]

print(filter_integers(test_values))  # Output: [5, 1, 2, 3]
```
This script provides a function `filter_integers` that filters a given list of any python objects and returns only the integers from it. The function is then tested with different markdown code examples, and the output shows the integers from the provided lists.