```python
def filter_integers(values): 
    return [x for x in values if type(x) == int]

# Test case: Filter integers from a list of various data types
print(filter_integers([1, 2, 3, 'abc', {}, [0] ])) 
``` 
This script defines a function `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list. The function employs a list comprehension with the `type()` built-in function to filter out non-integer values. 

This script provides a self-contained solution and passes corresponding tests for the `filter_integers` function.