```python
from typing import List
def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [i for i in values if type(i) == int]

# Test case 1: Filter values from the list
test_values = ['a', 3.14, 5]
print(filter_integers(test_values))  # Output: [5]

# Test case 2: Filter values from the list with mixed data types
test_values_mixed = [1, 2, 3, 'abc', {}, []]
print(filter_integers(test_values_mixed))  # Output: [1, 2, 3]

# Test case 3: Filter empty list
test_empty_list = []
print(filter_integers(test_empty_list))  # Output: []
```
The function filter_integers takes a list of values as input and returns a new list containing only the integers from the input list. This function is tested by using a list comprehension and the only integers will be added to the new list.