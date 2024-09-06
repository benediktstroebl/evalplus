```python
from typing import List
def filter_integers(values):
    """ Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 'three', (])
values2 = [1, 2, 3, 'abc', {}}
values3 = ['a', 3.14, 5]
print(filter_integers(values1))  # Output: []
print(filter_integers(values2))  # Output: [1, 2, 3]
print(filter_integers(values3))  # Output: [1, 3, 3. desired output is [1, 2, 3]
```  The function `filter_integers` takes a list of values as input and returns a new list containing only the integers from the original list.  The function uses the list comprehension and the `isinstance()` function to filter out non-integer values from the input list.