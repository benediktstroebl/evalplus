### Filter Integers from a List
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    
    Args:
    values (List[Any]): A list containing any type of Python values.
    
    Returns:
    List[int]: A list containing only the integers from the input list.
    
    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```
In this script, we define a function `filter_integers` that takes a list of any Python values as input. We then use a list comprehension to iterate over each value in the list and use the `isinstance` function to check if the value is an integer. If it is, we include it in the output list. The function returns this list of integers.