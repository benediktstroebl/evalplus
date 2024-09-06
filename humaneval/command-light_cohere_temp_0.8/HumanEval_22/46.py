```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = ['a', 3.14, 5]
print(filter_integers(values1))  # Output: [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))  # Output: [1, 2, 3]

# Test case 3
values3 = [1, 2, 3, 4, 'five', 6]
print(filter_integers(values3))  # Output: [1, 2, 3, 4, 6]
```

This script defines a function called `filter_integers` that filters a list of any Python values and returns a new list containing only the integers. The function uses a filtering technique based on the `isinstance` operator to only return integer values from the input list.