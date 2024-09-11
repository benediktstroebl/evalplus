```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list of python values.

    Returns:
    List[int]: A list of integers from the input.

    Example:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

This Python script uses list comprehension to filter out integers from a given list. The `isinstance()` function checks if each value in the list is an instance of the `int` class. The filtered list of integers is then returned by the function. The script includes docstrings for the function and example use cases to demonstrate its functionality. The test cases at the end are used to verify the correctness of the function.