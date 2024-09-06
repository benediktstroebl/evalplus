```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Basic integer filtering
values_test1 = ['a', 3.14, 5]
print(filter_integers(values_test1))  # Output: [5]

# Test case 2: Filter empty list
empty_list = []
print(filter_integers(empty_list))  # Output: []

# Test case 3: Filter non-integer elements
str_test = 'abc'
print(filter_integers([str_test]))  # Output: []

# Test case 4: Filter list with only integers
integers_only = [1, 2, 3, 4, 5]
print(filter_integers(integers_only))  # Output: [1, 2, 3, 4, 5]
```

This Python script defines a function called **filter_integers** that takes a list of values and returns a new list that contains only the integers from the original list. It is a series of test cases to validate the functionality of the function.