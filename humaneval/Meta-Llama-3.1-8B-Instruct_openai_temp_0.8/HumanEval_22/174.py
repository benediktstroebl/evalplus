```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any type of python values

    Returns:
        List[int]: A list of integer values

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [i for i in values if isinstance(i, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This Python script uses a list comprehension to create a new list containing only the integers from the input list. The `isinstance()` function is used to check if each element in the list is an integer. If it is, the element is included in the new list.