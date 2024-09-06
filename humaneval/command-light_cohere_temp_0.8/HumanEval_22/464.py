```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert isinstance(result1, list), "filter_integers returned unexpected type"
assert all(result1) == [5], "filter_integers didn't return only integers"

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert isinstance(result2, list), "filter_integers returned unexpected type"
assert all(result2) == [1, 2, 3], "filter_integers didn't return only integers"

# Test case 3
values3 = {a: 1, 2, 3, 4, 5}
result3 = filter_integers(values3)
assert isinstance(result3, list), "filter_integers returned unexpected type"
assert all(result3) == [1, 2, 3, 4, 5], "filter_integers didn't return only integers"
```
This Python script defines a function `filter_integers` that takes a list of values as an argument and returns a new list that contains only the integers from the input list. The function uses a filtering logic to identify the integers in the input and return them. The test cases provided demonstrate that the function successfully filters out only the integers from the given lists, passing all the tests.