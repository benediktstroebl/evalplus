```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.
    
    Args:
        values (List[Any]): A list containing any type of python values.
    
    Returns:
        List[int]: A list containing only the integers from the input list.
    """
    # Initialize an empty list to store the filtered integers
    filtered_values = []
    
    # Iterate over each value in the input list
    for value in values:
        # Check if the value is an integer
        if isinstance(value, int):
            # If it's an integer, append it to the filtered list
            filtered_values.append(value)
    
    # Return the filtered list of integers
    return filtered_values


# Test cases
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

Alternatively, you can use a list comprehension to achieve the same result in a more concise way:

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.
    
    Args:
        values (List[Any]): A list containing any type of python values.
    
    Returns:
        List[int]: A list containing only the integers from the input list.
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```