```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result
```

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out values that are not integers. It uses **isinstance()** function to check if each value in the list is of integer type, and if so, adds it to the `result` list. Finally, it returns the `result` list containing only the integer values. 

Here is an example usage of the function:
```python
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
```

This ensures that the result is a list of integers and handles the scenario where the input list contains a mixture of value types.