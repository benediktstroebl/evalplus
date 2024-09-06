```python
from typing import List

def filter_integers(values:
    """ Filters the input list of any python values for integers"""
    filtered_int = [x for x in values if isinstance(x, int)]
    return filtered_int

# Test cases
values1 = [1, 2, 3, 'abc', {}, [5, 6])
values2 = [1, 2, 3, 4, 'five', [], False]

print("Test Case 1: ", end="")
print(filter_integers(values1))
print()

print("Test Case 2: ", end="")
print(filter_integers(values2))
``` 
The function filter_integers in this code snippet takes a list of any Python values as an argument and returns a new list containing only the integers from the input list. It accomplishes this filter using the using a list comprehension and the isinstance() function to filter out the integers. The test cases demonstrate the the expected behavior of the function.