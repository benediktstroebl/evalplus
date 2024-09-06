```python
from typing import List

def filter_integers(values:
    return [int(element) for element in values if element.isinstance(int)]

filter_integers(['a', 3.14, 5])  # [5]
filter_integers([1, 2, 3, 'abc', {}, []])  # [1, 2, 3]
``` 
The provided code defines a function called **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. 

This is achieved by using a list comprehension with the **isinstance** function, which checks if each element is an instance of the built-in int class. 
The list comprehension iterates through each element in the input list and applies the condition if it is not an integer.