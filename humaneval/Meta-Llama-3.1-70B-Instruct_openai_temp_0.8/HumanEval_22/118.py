```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list of any python values

    Returns:
    List[int]: A list of integers filtered from the input list
    """
    # Initialize an empty list to store the filtered integers
    filtered_list = []

    # Iterate over each value in the input list
    for value in values:
        # Check if the value is an integer
        if isinstance(value, int):
            # If the value is an integer, append it to the filtered list
            filtered_list.append(value)

    # Return the filtered list of integers
    return filtered_list

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

Alternatively, you can use a list comprehension to achieve the same result in a more concise way:

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list of any python values

    Returns:
    List[int]: A list of integers filtered from the input list
    """
    # Use a list comprehension to filter the integers
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```