```python
from typing import List

def filter_integers(values:
    """ 
    filtered = [x for x in values if isinstance(x, int)]
    return filtered
``` 
The function takes a list of values and returns a new list containing only the integers from the input. 

The function uses the `isinstance` function to check if each value in the input list is an integer. 
The function then creates a new list called `filtered` and adds each value from the input list to the `filtered` list if the value is an integer. 
The function then returns the `filtered` list.