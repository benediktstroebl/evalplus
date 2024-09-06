```python
from typing import List

def filter_integers(values:
    """
        filtered = [int(_) for _ in values if _ != "" and type(_) == int]
    return filtered
``` 
This script defines a function `filter_integers` that takes a list of values as input and returns a new list that contains only the integers from the input. 

It uses list comprehension to iterate over each value in the input list and checks if the value is not an empty string and is of type `int`. If the condition is met, it adds the integer to the `filtered` list.