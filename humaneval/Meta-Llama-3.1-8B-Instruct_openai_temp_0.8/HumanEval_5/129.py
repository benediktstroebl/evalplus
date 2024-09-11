```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`
    
    Args:
        numbers (List[int]): The input list of integers
        delimiter (int): The number to insert between consecutive elements
    
    Returns:
        List[int]: The modified list with the delimiter inserted
    """
    if not numbers:
        # If the input list is empty, return it as is
        return numbers
    
    result = [numbers[0]]
    
    for num in numbers[1:]:
        # Append the delimiter to the result list, then append the current number
        result.extend([delimiter, num])
    
    return result[:-1]  # Remove the extra delimiter at the end

# Example usage
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that inserts a specified delimiter between consecutive elements of an input list. It handles the edge case where the input list is empty and preserves the original list's elements, but with the delimiter inserted between them. The function then demonstrates its usage with example inputs.