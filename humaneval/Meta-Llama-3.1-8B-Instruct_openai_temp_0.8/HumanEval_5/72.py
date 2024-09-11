```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between elements

    Returns:
        List[int]: The list with 'delimeter' inserted between elements
    """
    if not numbers:
        # If the input list is empty, return an empty list
        return []
    
    result = []
    for i, num in enumerate(numbers):
        # Append each number from the input list
        result.append(num)
        
        # If it's not the last number in the list, append the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This Python script implements the function `intersperse` which takes a list of integers `numbers` and an integer `delimeter` as input. It inserts the `delimeter` between every two consecutive elements of `numbers` and returns the resulting list. The script includes two test cases at the end to verify the function's correctness.