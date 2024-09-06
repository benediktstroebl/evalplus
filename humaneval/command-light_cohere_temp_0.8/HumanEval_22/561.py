```python
def filter_integers(values):
    """ Filter given list of any python values and return only integers"""
    return [x for x in values if isinstance(x, int)]

# Tests cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, 2, 'abc', '123']))  # []
print(filter_integers([1, 2, 3. }))  # [1, 2, 3]
```