```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script defines a function `filter_integers` that takes a list of any Python values as input and returns a new list containing only the integers from the original list. The function uses a list comprehension to iterate over the input list and check each value using the `isinstance` function. If a value is an instance of `int`, it is included in the new list.

The script also includes test cases to demonstrate the function's behavior. When run, the script will print the expected output for the given test cases.