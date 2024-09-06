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

This function takes a list of various Python values and returns a list of integers that were present in the input list. It does so by using a list comprehension that checks if each value in the input list is an instance of the int class, and if so, including it in the output list. The function includes type annotations that help developers understand the expected input and output types.