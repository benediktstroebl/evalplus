```python
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([1, 2, '3', 4, 'hello'])))  # Output: []
print(filter_integers([1, 2, 3. Birch, 4, 'gold']))  # Output: [1, 2, 3]
```