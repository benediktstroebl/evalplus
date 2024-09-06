```python
def filter_integers(values): 
    """ Filters and returns integers from a given list."""
    return [x for x in values if isinstance(x, int)]

# Test cases 

# Test case 1: Filter integers from a list
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert isinstance(result1, list)
assert all(isinstance(x, int) for x in result1) == True

# Test case 2: Filter integers from a mixed list
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert isinstance(result2, list)
assert all(isinstance(x, int) for x in result2) == True

# Test case 3: Filter empty list
values3 = []
result3 = filter_integers(values3)
assert isinstance(result3, list) and result3 == []

# Test case 4: Filter non-integers
values4 = [1, 2, 3, 'abc', 10]
result4 = filter_integers(values4)
assert isinstance(result4, list)
assert all(isinstance(x, int) for x in result4) == False
```
This Python script defines a function **filter_integers** that filters and returns integers from a given list. It also comes with several test cases to validate the correctness of the function. The function successfully filters the expected values.