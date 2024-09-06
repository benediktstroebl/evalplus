Here is a self-contained Python function that solves the problem of filtering integers from a list of various types:
```python
def filter_integers(values):
    result = [x for x in values if isinstance(x, int)]
    return result

# Test case 1
test_values1 = ['a', 3.14, 5]
result1 = filter_integers(test_values1)
assert result1 == [5]

# Test case 2
test_values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(test_values2)
assert result2 == [1, 2, 3]
```

This function, named `filter_integers`, takes a list of values as input and uses a list comprehension to filter out only the elements that are instances of the built-in `int` class. 
This function can be easily reused and tested for different sets of values.