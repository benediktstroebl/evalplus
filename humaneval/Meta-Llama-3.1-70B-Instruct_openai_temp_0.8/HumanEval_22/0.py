```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.
    
    Args:
    values (List[Any]): A list of any python values.
    
    Returns:
    List[int]: A list of integers from the given list.
    """
    # Initialize an empty list to store the filtered integers
    filtered_values = []
    
    # Iterate over each value in the given list
    for value in values:
        # Check if the value is an integer
        if isinstance(value, int):
            # If the value is an integer, add it to the filtered list
            filtered_values.append(value)
    
    # Return the filtered list of integers
    return filtered_values


# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of any python values as input, filters out the integers, and returns them in a new list. It uses the built-in `isinstance` function to check if a value is an integer. The test cases at the end demonstrate the function's usage and expected output. 

Alternatively, you can use list comprehension to achieve the same result in a more concise way:

```python
def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]
```