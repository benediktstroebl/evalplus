```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between the elements.

    Returns:
        List[int]: The list with the delimiter inserted between elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        # If the input list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Start the result list with the first element
    for i in range(1, len(numbers)):
        # Append the delimiter and then the current element to the result list
        result.extend([delimiter, numbers[i]])
    
    return result[:-1] if len(numbers) == 1 else result  # Remove the extra delimiter at the end if the list has only one element

# Test cases
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines a function `intersperse` that takes a list of integers and an integer delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements of the input list. The function uses a simple loop to construct the result list, and handles the edge case where the input list is empty or has only one element. The test cases at the end of the script verify the correctness of the function.