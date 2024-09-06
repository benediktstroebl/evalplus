```python
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

# Test cases for function
values1 = ['a', 3.14, 5]
print(filter_integers(values1))  # Output ['5']

values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))  # Output [1, 2, 3]

values3 = [1, 2, 3, 'a', 4]
print(filter_integers(values3))  # Output [1, 2, 3]

values4 = [1, 2, 3, 'ab', {'c': 4, "d": 5}]
print(filter_integers(values4))  # Output ['1', '2', '3', 'ab', {'c': 4, 'd': 5}]
```

The function filter_integers accepts a list of values and returns a new list that contains only the integers from the original list. It uses the Filtering based on the isinstance() condition.