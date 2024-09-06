Here is a self-contained Python script with a function that filters integers from a list of various types:
```python
from typing import List

def filter_integers(values:
    return [int(el) for el in values if el.is_integer()]
```

This script provides a function that takes a list of values and returns a new list containing only the integers from the input list. The function uses a `is_integer()` method to filter the values, which checks if each element in the list is an integer. The `is_integer()` method returns `True` if the element is an integer, and `False` otherwise.