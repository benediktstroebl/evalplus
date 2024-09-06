Here's the self-contained Python function that filters integers from a given list: 
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert len(result1) == 2

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert len(result2) == 3

# Test case 3
values3 = [1, 2, 3, True, [], 0]
result3 = filter_integers(values3)
assert len(result3) == 3
```
This function is designed to accept a list of values and return a new list where all values are converted to integers. It uses Python'sstr to iterate through the list and filter out the values that are not of type int. 
This function is self-contained and can be used to solve the problem of filtering integers from a given list of values.