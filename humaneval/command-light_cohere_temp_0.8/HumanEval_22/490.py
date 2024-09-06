```python
def filter_integers(values):
    """ Filter given list of any python values and return only integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = ['a', 3.14, 5]
print(filter_integers(values1))  # Output: [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))  # Output: [1, 2, 3]

# Test case 3
values3 = [1, 2, 3, 'abc', [1, 2, 3, 4, 5], []]
print(filter_integers(values3))  # Output: [1, 2, 3, 4, 5]
```
The function `filter_integers` takes a list of values as input and returns a new list that contains only the integers from the input list. 

It uses a list comprehension to iterate through each element in the input list, and checks if the element is an instance of the integer type (`int`). If it is, then the element is included in the new list.