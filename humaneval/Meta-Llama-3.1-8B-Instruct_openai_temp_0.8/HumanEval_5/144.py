```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between the elements of the list

    Returns:
        List[int]: The list with the delimeter inserted

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # Check if the list is empty
        return []
    
    result = [numbers[0]]  # Initialize the result list with the first element of the input list
    for i in range(1, len(numbers)):  # Iterate over the input list starting from the second element
        result.extend([delimeter, numbers[i]])  # Append the delimeter and the current element to the result list
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter as input, and returns the list with the delimeter inserted between every two consecutive elements. The function uses a simple loop to iterate over the input list, and appends the delimeter and the current element to the result list. The script also includes a test case to verify the correctness of the function.