```python
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert len(result1) == 2

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert len(result2) == 3

# Test case 3
values3 = [1, 2, 3, [0, 1], ['a', 'b'], None]
result3 = filter_integers(values3)
assert len(result3) == 4
```
The function `filter_integers` takes a list of values as input and returns a new list containing only the integers from the input list.  The integers are filtered from the list using list comprehension.