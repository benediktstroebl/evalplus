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

# Tests:
values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # Output: [1, 2, 3]
``` 

The function `filter_integers` takes a list of values of any type and returns a list of integers. It iterates through each value in the input list, and if the value is an integer, it is added to the result list. Finally, the function returns the result list containing only the integers from the original list.