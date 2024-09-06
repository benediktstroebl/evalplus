```python
from typing import List

def filter_integers(values):
    return [x for x in values if type(x) == int]

filter_integers(['a', 3.14, 5]) # [5]
filter_integers([1, 2, 3, 'abc', {}, []]) # [1, 2, 3]
filter_integers([4, 'four', 2.0]) # []
 []
``` 
This script defines a function **filter_integers** that takes a list of values as an argument and returns a new list containing only the integers from the original list. 

The function uses the typing module to ensure type-checking, and the list comprehension function to filter the list for integers.