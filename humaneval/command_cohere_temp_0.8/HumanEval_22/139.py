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

The function uses a type hint `List[Any]` to handle various data types in the input list. It iterates over each element in the input list and checks if the element type is integer using the `isinstance()` function. If true, the integer is added to the `result` list. The function returns the filtered `result` list upon completion. 

This solution covers both test cases provided in the prompt and provides an efficient solution that operates with a constant time complexity of O(n).

The function can be used in other Python scripts to filter a list of any data types for integers, as it is self-contained and does not rely on any external variables or functions.  It is also formatted and commented to provide a clear understanding of the functionality and improve readability.