```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with different input values and assert the expected output
values_list = [['a', 3.14, 5, 1, 2, 'abc', {}, []]
assert filter_integers(values_list) == [5, 1, 2, 3]

# Another test with different data types to ensure the function handles it correctly
mixed_types_values = [['a', 3.14, 'string', 5, (6), (7)]
assert filter_integers(mixed_types_values) == [3, 5, 6, 7]

# Test with an empty list
empty_values = []
assert filter_integers(empty_values) == []

# Test with complex data structures to ensure the function works with non-trivial cases
complex_struct = {['a': 1, 'b': [2, 'c'], 'd': 3, 'e': 'f']}
assert filter_integers(complex_struct) == [1, 'c', 3]
```
This script defines a function `filter_integers` that filters a given list of values to include only integers. It then passes several tests to this function with different sets of values and asserts that the expected output is correct.