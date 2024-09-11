```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))  # Should print: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Should print: [1, 2, 3]
```

This script defines a function `filter_integers` that uses a list comprehension to create a new list containing only the integer values from the input list. The `isinstance(value, int)` function checks if a value is an integer. The function is then tested with two example inputs to verify its correctness.