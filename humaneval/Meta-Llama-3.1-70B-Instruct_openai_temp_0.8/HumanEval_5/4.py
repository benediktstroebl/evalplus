```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): The input list of numbers.
    delimiter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
    List[int]: The modified list with 'delimiter' inserted between every two consecutive elements.
    """
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i, num in enumerate(numbers):
        # Append the current number to the result list
        result.append(num)
        
        # If it's not the last number in the list, append the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    
    # Return the modified list
    return result

# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```