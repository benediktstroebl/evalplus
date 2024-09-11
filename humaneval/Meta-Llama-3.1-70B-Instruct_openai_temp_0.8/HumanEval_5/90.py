```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
    numbers (List[int]): The input list of integers.
    delimiter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
    List[int]: The modified list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        # Add the current number to the result list
        result.append(num)
        
        # If it's not the last number in the list, add the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    
    return result


# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input. It iterates over the input list, adding each number to the result list and inserting the delimiter between every two consecutive numbers. The function returns the modified list.

The script also includes test cases to verify the correctness of the function. The test cases cover the empty list scenario and a list with multiple elements.