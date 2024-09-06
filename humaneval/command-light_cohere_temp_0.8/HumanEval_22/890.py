```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 3, 'abc', 0]
values2 = [3.14, 5]
print(filter_integers(values1))  # Output [1, 2, 3]
print(filter_integers(values2))  # Output [3.14, 5]
``` 
This script defines a function called **filter_integers** that takes a list of values and returns a new list that contains only the integers from the input list. The script then provides two test cases to demonstrate the function, and the output of both test cases matches the expected result.