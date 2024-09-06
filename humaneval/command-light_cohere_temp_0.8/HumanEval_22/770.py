```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with a variety of values
values_test = [
    ['a', 3.14, 5], [1, 2, 3, 'abc', }, [1, 2, 3], [{}, []]
]

print(filter_integers(values_test))  # Prints [5, 1, 2, 3]
``` 
This function, `filter_integers`, takes a list of values as input and returns a new list containing only the integers from the input list. 

The `isinstance` operator is used to check if each element in the input list is an integer. The function then returns a list of integers.