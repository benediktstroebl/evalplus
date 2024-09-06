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
assert filter_integers(['a', 3.14, 5]) == [5]
assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
``` 

This code snippet utilizes the `typing` module to improve type safety and provide more information to developers via the function signature. The function `filter_integers` takes a list of any Python values as input and returns a list of integers. It initializes an empty list `result` to store the filtered integers, and then loops through each value in the input list. If the current value is an integer, it is added to the `result` list. The function returns the final list of filtered integers. 

The tests assert that the function correctly filters out non-integer values from the input list, demonstrating the behavior of the function with different inputs.  This approach provides better code readability, maintainability, and helps to catch potential type-related bugs early during development.