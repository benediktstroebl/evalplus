```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of values that can be of any type

    Returns:
        List[int]: A list of integers from the input list

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


# Test the function
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))
    print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script uses a list comprehension to create a new list `x` that includes only the integers from the input list `values`. The `isinstance(x, int)` function is used to check if each value is an integer.

When you run this script, it will print the results of the `filter_integers` function for the two test cases.