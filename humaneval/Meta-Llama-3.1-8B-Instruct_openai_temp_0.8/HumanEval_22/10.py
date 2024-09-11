```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list containing any type of python values

    Returns:
        List[int]: A list of integers filtered from the input list

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Example usage:
numbers = [1, 2, 'three', 4.0, 5]
filtered_numbers = filter_integers(numbers)
print(filtered_numbers)  # Output: [1, 2, 5]
```

This script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integers from the original list. The function uses a list comprehension to achieve this.

The `isinstance(x, int)` function is used to check if a value is an integer. If it is, the value is included in the new list.

Finally, the script includes an example usage of the function with a list of mixed values and prints the filtered list.