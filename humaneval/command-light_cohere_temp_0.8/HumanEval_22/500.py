```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers."""
    return [int(x) for x in values if x.isdigit()]
print(values)
```
The code defines a function called `filter_integers` that takes a list of values as an argument and returns a new list containing only the integers from the input list. The function utilizes a Python's built-in `isdigit()` function to check if each element in the input list is a digit, and then converts the element to an integer using `int()` if it is indeed a digit. 

This self-contained function demonstrates a common Python task of filtering and transforming data in a concise and readable manner.