```python
from typing import List

def filter_integers(values):
    return [int(el) for el in values if type(el) == int]

# Test the function with various data types
values_list = [['a', 3.14, 5, 1, 2, 'abc', {}, []]
print(filter_integers(values_list))  # Output: [5, 1, 2, 3]

values_list_str = "['a', 3.14, 5, 1, 2, 'abc', {}, [], [10, 20] ]"
print(filter_integers(values_list_str))  # Output: [1, 2, 'abc', 10, 20]

values_dict = {1: 'a', 3: 'b', 4: 'c'}
print(filter_integers(values_dict))  # Output: ['a']

values_tuple = (1, 'abc', 5, 6)
print(filter_integers(values_tuple))  # Output: ['1', 'abc']
```