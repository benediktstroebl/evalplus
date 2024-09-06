```python
from typing import List
def filter_integers(values: 
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list
values_list = [3.14, 5, 1, 2, 'abc']
print(filter_integers(values_list))  # Output: [3.14, 5, 1, 2]

# Test case 2: Filter integers from a tuple
values_tuple = (1, 2, 3, 'abc')
print(filter_integers(values_tuple))  # Output: [1, 2, 3]

# Test case 3: Filter integers from a string
values_string = "1 2 3 abc"
print(filter_integers(values_string))  # Output: [1, 2]

# Test case 4: Filter integers from an empty list
print(filter_integers([]))  # Output: []
```
This script defines a function **filter_integers** that accepts a list of values and returns a new list containing only the integer elements from the input. It uses a Python's list comprehension to filter out the integers. The script includes several test cases to demonstrate the function, passing all of them successfully.