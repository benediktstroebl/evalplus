```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [1, 2, 3, 'abc', {}, [0, None, '123']]
print(filter_integers(values))  # Output: [1, 2, 3]
``` 
This Python code defines a function `filter_integers` that takes a list of values as an argument and returns a new list containing only the integer elements from the input list. The function uses the basic list comprehension and the `isinstance` condition to filter out non-integer elements. The output of the filter_integers function is a list with the elements 1, 2, and 3, which are the only integer elements in the input list.