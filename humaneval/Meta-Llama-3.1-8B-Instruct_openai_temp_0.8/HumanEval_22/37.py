```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): A list of values of any type
    
    Returns:
        List[int]: A list of integers from the input list
    
    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Testing the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

In this script, we define the `filter_integers` function which uses a list comprehension to filter the input list for integer values. The `isinstance(value, int)` function checks if a given value is of type `int`. We then print the results of the function with some example inputs to verify that it works correctly.