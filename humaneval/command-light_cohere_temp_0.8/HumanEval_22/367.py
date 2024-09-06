```python
from typing import List

def filter_integers(values:
    """
    filtered_ints = []
    for value in values:
        if isinstance(value, (int)):
            filtered_ints.append(value)
    filtered_ints
    return filtered_ints

# Example usage:
values = [1, 2, 3, 'abc', {}, [5], [123, 456]]
result = filter_integers(values)
print(result)
``` 
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input list. 

The function uses a for-loop to iterate through the input list and checks if each value is an integer using the `isinstance` function. 

The function then creates a new empty list called `filtered_ints` and appends any integer values to it.