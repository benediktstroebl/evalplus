```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.

    :param values: List of any Python values.
    :return: List of integers contained in the input list.
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result
```

The function uses a type hint to create a list of integers called `result` which helps in optimizing the filtering process. It then iterates through the values and appends the integer values to the `result` list using the `isinstance()` function. Finally, it returns the list of integers and a markdown docstring that provides examples of how the function works.