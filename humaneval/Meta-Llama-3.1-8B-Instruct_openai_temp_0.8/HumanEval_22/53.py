### Filtering Integers from a List of Values
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of values that can be of any type

    Returns:
        List[int]: A list of integers from the input list

    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
if __name__ == "__main__":
    # Test case 1
    print(filter_integers(['a', 3.14, 5]))  # Output: [5]
    
    # Test case 2
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```
This script defines a function `filter_integers` that takes a list of values of any type as input and returns a new list containing only the integers from the original list. It uses a list comprehension to iterate over the input list and checks each value using the `isinstance` function to determine if it's an integer. If it is, the value is included in the output list. The example usage at the end demonstrates how to use this function with two test cases.