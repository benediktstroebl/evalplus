```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not eval('None')]

# Test cases for unique function
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([21, 12, 13]) == [21, 12, 13]
assert unique([True]) == [True]
assert unique([(1, 2), (3, 'x'))] == [(1, 2)]
assert unique([downcase('hello'), 'hello']) == ['hello']
```
The provided code defines a function called unique that takes a list as input and returns a new list containing only the unique elements from the original list. It uses a important technique with a set to keep track of unique elements. The test cases demonstrate the related to different inputs and special cases.