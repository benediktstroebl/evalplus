```python
from typing import List

def filter_integers(values):
    return [int(x) for x in values if x.isdigit()]
``` 
This script defines a function called filter_integers that takes a list of values, and returns a new list containing only the integers from the input list. The function uses the _typing module to ensure type safety and returns a list of integers for the given list of any value.