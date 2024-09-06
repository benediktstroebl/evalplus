```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers
```

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out all elements that are not of type `int`. It uses a list comprehension that iterates through each value in the input list. If the current item is an instance of the integer class, it is appended to the `integers` list, and all other types are excluded from the result. The function's docstring contains usage examples that illustrate its behavior.