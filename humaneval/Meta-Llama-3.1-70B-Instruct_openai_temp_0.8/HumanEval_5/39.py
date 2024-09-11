```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The resulting list with the delimiter inserted.
    """
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i, num in enumerate(numbers):
        # Add the current number to the result list
        result.append(num)
        
        # If it's not the last number in the list, add the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    
    # Return the resulting list
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements of the input list. The function uses a simple loop to iterate over the input list and append each number and the delimiter (if necessary) to the result list. The test cases demonstrate the function's behavior with an empty list and a non-empty list.