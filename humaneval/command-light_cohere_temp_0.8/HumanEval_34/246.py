```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(l))

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
asdf = ['foo', 'bar', 'foo', 'baz', 'qux']
assert unique(asdf) == ['foo', 'bar', 'baz', 'qux']
```  This function uses the set() function to remove duplicate elements and the list() constructor to convert the set into a list.