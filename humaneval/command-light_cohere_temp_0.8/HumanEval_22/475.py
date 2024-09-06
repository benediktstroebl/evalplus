```python
from typing import List

def filter_integers(values:
        return [int(x) for x in values if x.isinstance(int)]
```
This function takes a list of any python values and returns a new list of integers from the input list. 

It uses the `isinstance()` method to check if each value in the input list is an instance of the `int` class, which is a special class in Python that represents integer numbers. 

The function then uses a list comprehension to create a new list containing only the integer values from the original list. 

Note: This function assumes that the input list contains only valid Python values, and does not perform any type checking or error handling beyond basic type conversions.