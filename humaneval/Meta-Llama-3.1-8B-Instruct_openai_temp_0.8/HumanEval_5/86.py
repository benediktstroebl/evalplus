```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The list with the delimiter inserted between elements.
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Start the result list with the first element of the input list
    
    for i in range(1, len(numbers)):  # Iterate over the rest of the list
        result.append(delimiter)  # Insert the delimiter
        result.append(numbers[i])  # Append the current element
    
    return result


# Example use cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function, which inserts a specified number between every two consecutive elements of the input list. The function handles the edge case where the input list is empty and includes example use cases in the script.