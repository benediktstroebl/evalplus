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

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out values that are not of type `int`. It uses Python's `typing` module to declare the input parameter as `List[Any]` and the return value as `List[int]`. The function iterates over each value in the input list, and if the value is an integer, it is added to the `result` list. Finally, the function returns the `result` list containing only the integers from the original input list.  This approach ensures that the function only accepts lists as input and returns a list of integers as expected.