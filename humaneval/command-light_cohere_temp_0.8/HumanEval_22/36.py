```python
from typing import List

def filter_integers(values: List[Any]):
    return [i for i in values if type(i) == int]

# Test the function with various input values
print(filter_integers(['a', 3.14, 5]))      # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []])) # [1, 2, 3]
print(filter_integers([1, 2, 'abc', 3, 'black'])) # []
print(filter_integers([11, 22, 11, 33]))   # [11, 22]
``` 
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the original list. The function uses a filtering logic to iterate over each element in the input list and only keeps integers, which are then converted to an integer type.