```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.
    
    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to insert between consecutive elements.
    
    Returns:
    List[int]: The modified list with the delimeter inserted between consecutive elements.
    """
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i, num in enumerate(numbers):
        # Add the current number to the result list
        result.append(num)
        
        # If it's not the last number in the list, add the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    
    # Return the modified list
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```