```python
def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
values_test1 = ['a', 3.14, 5]
print(filter_integers(values_test1))  # [5]

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test2))  # [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses a boolean list comprehension to filter out the elements that are not integers. The output of this function is then tested with two different lists, and the results match the expected output.