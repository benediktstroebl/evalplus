```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # [5]

values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # [1, 2, 3]

values = [1, 2, 3, 'a', 4, 5]
print(filter_integers(values))  # [1, 2, 3, 'a', 4, 5]

values = [1, 2, 'abc', 3]
print(filter_integers(values))  # []
```