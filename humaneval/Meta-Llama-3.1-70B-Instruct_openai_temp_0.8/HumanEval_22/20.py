```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list containing any python values.

    Returns:
    List[int]: A list containing only integers from the input list.
    """
    # Initialize an empty list to store the filtered integers
    filtered_values = []

    # Iterate over each value in the input list
    for value in values:
        # Check if the value is an integer using the isinstance function
        if isinstance(value, int):
            # If the value is an integer, append it to the filtered list
            filtered_values.append(value)

    # Return the filtered list of integers
    return filtered_values


# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

Alternatively, you can use a list comprehension to make the function more concise:

```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list containing any python values.

    Returns:
    List[int]: A list containing only integers from the input list.
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```