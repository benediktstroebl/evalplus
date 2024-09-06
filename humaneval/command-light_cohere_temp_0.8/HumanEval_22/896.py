```python
def filter_integers(values): 
    """ Filter given list of any python values only for integers"""

    return [x for x in values if isinstance(x, int)]

# Test case 1: Basic Integer Filter
print(filter_integers(['a', 3.14, 5]))  # [5]

# Test case 2: Filter empty list
print(filter_integers([ ]))  )  # []

# Test case 3: Filter List with Data Types
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]

# Test case 4: Filter complex objects
print(filter_integers([1, 2, 3, 'abc, true, (42)]))  # [1, 2, 3]
```
The function filter_integers takes a list of values as input and returns a new list containing only the integers from the input list. This is using the filter_integers function, you can quickly filter out the integers from any given list, making it useful for various scenarios.