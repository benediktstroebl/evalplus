```python
from typing import List

def filter_integers(values:
    """
    filtered_ints = [int(item) for item in values if item.isinstance(int)]
    return filtered_ints
``` 
This Python function, `filter_integers`, takes a list of values as an argument and returns a new list that contains only the integers from the input list. The function uses a `isinstance()` to check if each element in the list is an instance of the built-in `int` class. This ensures that only integer values are retained in the output list.