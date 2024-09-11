```python
from typing import List, Any
from typing import Any  # Import Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): List of any python values.

    Returns:
        List[int]: Filtered list of integers.
    """
    return [value for value in values if isinstance(value, int)]  # Filter values using list comprehension

# Test cases
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
    print(filter_integers([1, 2, 'a', 3.14, 5]))  # Output: [1, 2, 5]
    print(filter_integers([]))  # Output: []
```

This script defines a function `filter_integers` that takes a list of any Python values as input and returns a new list containing only the integers from the original list. It uses a list comprehension to create the filtered list, which is more concise and readable than a traditional for loop. The test cases at the end demonstrate the function's behavior with different inputs.