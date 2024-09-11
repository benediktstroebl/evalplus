```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): A list containing any type of python values
    
    Returns:
        List[int]: A list of integers filtered from the given list
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script defines a function `filter_integers` that uses a list comprehension to iterate over each value in the input list. It uses the `isinstance` function to check if a value is an integer, and if so, includes it in the output list.

You can run this script as a standalone Python program, and it will output the results of the two test cases.