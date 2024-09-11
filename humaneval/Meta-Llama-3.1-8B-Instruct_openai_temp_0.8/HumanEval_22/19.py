```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): A list of values of any type
    
    Returns:
        List[int]: A list of integers from the input list
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of values of any type and returns a new list containing only the integers from the original list. The function uses a list comprehension with the `isinstance` function to filter the values.

The test cases are run at the end of the script using the `if __name__ == "__main__":` block. This block is used to ensure that the test cases are only run when the script is executed directly (i.e., not when it is imported as a module by another script).