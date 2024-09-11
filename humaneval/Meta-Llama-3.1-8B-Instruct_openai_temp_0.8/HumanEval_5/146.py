```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to insert between elements.

    Returns:
        List[int]: The list with the delimeter inserted between elements.
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers

    result = [numbers[0]]  # Start the result with the first element
    for i in range(1, len(numbers)):  # Iterate over the rest of the list
        result.append(delimeter)  # Insert the delimeter before the current element
        result.append(numbers[i])  # Append the current element

    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter integer as input, and returns a new list with the delimeter inserted between every two consecutive elements. The function uses a simple iteration over the input list to achieve this. The test cases at the end demonstrate the function's behavior with both an empty list and a list with multiple elements.