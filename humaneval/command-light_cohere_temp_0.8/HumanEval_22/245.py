```python
from typing import List

def filter_integers(values:
    """ 
    filtered = [x for x in values if isinstance(x, int)]
    return filtered
``` 
This script defines a function called filter_integers that takes a list of values and returns a new list that contains only the integers from the input list. The function uses a Python's built-in `isinstance` function to check the type of each element in the list, and uses a list comprehension to filter out the integers.