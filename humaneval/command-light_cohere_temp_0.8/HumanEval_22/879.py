```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test = [1, 2, 3, 'abc', 3.14, 5]
print(filter_integers(values_test))  # [1, 2, 3, 5]

empty_list = []
print(filter_integers(empty_list))  # []

list_with_string = [1, 2, 'abc]
print(filter_integers(list_with_string))  # ['abc']

large_value = 123456
print(filter_integers([large_value]))  # [123456]
``` 
This code defines a function **filter_integers** that filters a given list for only the integers. It uses a operator **in to filter out the non-integer elements. The test cases show how the _filter_integers_ function works.