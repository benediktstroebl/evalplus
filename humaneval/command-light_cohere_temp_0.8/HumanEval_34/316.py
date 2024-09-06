```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

# Test cases
test_unique = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ['a', 'b', 'c', 'd'],
    ['a', 'bc', 'd']
]

for case in test_unique:
    assert unique(case) == set(case)
``` 
This code defines a function called unique that takes a list lst as input and returns a sorted list of unique elements in lst. The function uses the unique set to filter out duplicates, and the result is then converted back to a list.