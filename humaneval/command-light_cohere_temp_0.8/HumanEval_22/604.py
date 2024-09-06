```python
from typing import List

def filter_integers(values):
    return [x for x in values if type(x) == int]

print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
``` 
This script defines a function **filter_integers** that takes a list of any Python value and returns a new list that contains only the integers from the input list. The function uses a list comprehension with the "if" statement to filter out the non-integer elements from the input list.