```python
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = ['a', 3.14, 5]
assert filter_integers(values1) == [5]

values2 = [1, 2, 3, 'abc', {}, []]
assert filter_integers(values2) == [1, 2, 3]

values3 = [1, 2, 3, 4, 5, 6]
assert filter_integers(values3) == [1, 2, 3, 4, 5]

# pass when called with non list arguments
result = filter_integers('abc')
assert result == []

result = filter_integers([10, 20])
assert result == []
```