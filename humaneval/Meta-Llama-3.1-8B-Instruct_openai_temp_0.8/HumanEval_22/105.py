```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any Python values

    Returns:
        List[int]: A list of integers from the input list

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    # Use list comprehension to filter integers from the list
    return [value for value in values if isinstance(value, int)]

# Test the function
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

This script uses the `isinstance()` function to check if each value in the list is an integer, and then uses list comprehension to create a new list containing only the integers. The `if __name__ == "__main__"` block is used to test the function with example inputs.