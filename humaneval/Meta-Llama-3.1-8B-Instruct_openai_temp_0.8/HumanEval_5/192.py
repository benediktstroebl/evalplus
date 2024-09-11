### Interspersing Numbers in a List
#### Python Script

```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between elements.

    Returns:
        List[int]: The list with the delimeter inserted.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # Check if the list is empty
        return numbers
    
    result = [numbers[0]]  # Start with the first element of the list
    for i in range(1, len(numbers)):  # Iterate over the rest of the list
        result.append(delimeter)  # Insert the delimeter
        result.append(numbers[i])  # Add the current element
    return result


# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines a function `intersperse` that inserts a specified number (`delimeter`) between every two consecutive elements of a given list (`numbers`). The function handles the case where the input list is empty and returns the modified list. It uses a simple iterative approach to build the resulting list. The script includes example use cases to demonstrate the function's behavior.