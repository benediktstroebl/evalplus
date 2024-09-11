```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.

    Args:
    values (List[Any]): A list of any Python values.

    Returns:
    List[int]: A list of integers from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5])) # Expected output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []])) # Expected output: [1, 2, 3]
    print(filter_integers([1, 2, 'three', 4.5, 'five'])) # Expected output: [1, 2, 4]
```

In this code:

*   We define a function `filter_integers` that takes a list of any Python values as input.
*   We use a list comprehension to filter out only the integers from the input list. The `isinstance` function checks if a value is an instance of the `int` class.
*   We include test cases in the `if __name__ == "__main__":` block to verify the function's behavior with different inputs.