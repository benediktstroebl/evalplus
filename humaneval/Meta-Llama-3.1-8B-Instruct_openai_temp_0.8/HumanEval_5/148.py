```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): Number to be inserted between elements

    Returns:
        List[int]: List with delimeter inserted between elements

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = []
    for num in numbers:
        result.append(num)
        if result:  # Check if result list is not empty
            result.append(delimeter)
    return result[:-1] if result else result  # Remove the last delimeter if list is not empty


# Test the function
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a Python function named `intersperse` that inserts a specified number (`delimeter`) between every two consecutive elements of an input list (`numbers`). The function iterates over the list, appends each number to the result list, and then appends the `delimeter`. The function returns the result list, removing the last `delimeter` if the input list is not empty.