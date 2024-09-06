```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
``` 
This function takes a list of values and returns a new list containing only the integers from the input list. 

It uses a list comprehension with a condition that checks if each element in the list is an integer, and if it is, it is included in the new list.