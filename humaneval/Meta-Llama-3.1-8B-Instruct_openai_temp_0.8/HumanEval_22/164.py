```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): A list of any python values
    
    Returns:
        List[int]: A list of integers from the input list
    
    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))
    print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

In this script, the `filter_integers` function uses a list comprehension to iterate over the input list and include only the values that are instances of the `int` type. The `isinstance` function is used to check the type of each value. The script also includes doctests to verify the function's behavior.