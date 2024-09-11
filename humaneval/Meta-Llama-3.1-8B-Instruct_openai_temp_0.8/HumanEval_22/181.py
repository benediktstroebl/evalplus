```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Use a list comprehension to create a new list that includes only the integers from the input list
    return [value for value in values if isinstance(value, int)]


# Example usage
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

In this script, we define the `filter_integers` function that takes a list of values of any type and returns a new list that includes only the integers from the input list. We use a list comprehension to create the new list, and the `isinstance` function to check whether each value is an integer. Finally, we demonstrate the function's usage with two example calls.