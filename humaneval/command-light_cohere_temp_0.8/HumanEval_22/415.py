Here is a self-contained Python function that filters integers from a given list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
test_cases = [[values] * values for values in test_values]

assert filter_integers(test_cases[0]) == [5]
assert filter_integers(test_cases[1]) == [1, 2, 3]
assert filter_integers(test_cases[2]) == [1, 2, 3]

```
This function, `filter_integers`, takes a list of values and returns a new list containing only the integers from the input. It uses Python'sFC's `isinstance` function to check if each value in the list is an integer.