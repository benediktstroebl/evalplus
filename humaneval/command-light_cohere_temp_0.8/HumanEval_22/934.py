```python
from typing import List

def filter_integers(values:
    return [int(element) for element in values if element.isdigit()]
``` 
This function uses the `isdigit()` method to check if each element in the input list is a digit, and then converts that element to an integer using `int()` before returning the list of integers.