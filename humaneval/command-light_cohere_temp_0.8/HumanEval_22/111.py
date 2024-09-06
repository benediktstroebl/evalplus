```python
from typing import List

def filter_integers(values:
    return [int(x) for x in values if x.isinstance(int)]
```
This Python code defines a function called `filter_integers` that takes a list of values as input and returns a new list containing only the integer elements from the original list. 

The function uses the `isinstance(int)` function to check if each value in the list is an instance of the `int` built-in class, which represents integer numbers. 

This way, it effectively filters out non-integer values from the input list and returns a new list containing only the integers. 

The function is self-contained, as it does not require any additional arguments or external variables and provides a clear and concise return statement. 
The function is useful for filtering a list of values based on their type, specifically for integers, and can be applied to various types of input data.