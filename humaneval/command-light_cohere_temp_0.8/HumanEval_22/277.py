```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values for integers

    Args: values (List[Any]): List of elements with potential elements of any data type

    Returns: List[int]: A new list with filtered integers
    """
    return [num for num in values if num != '' and num.isinstance(int)]
```
The filter_integers function in this script accepts a list of any Python values as an argument and outputs a new list containing just the integers. 
The function filters out any non-integer values and empty strings from the input list by using list comprehension and the isninstance() function. 
This function is self-contained, meaning it doesn't require any external functions or variables to solve the problem and pass the tests.