```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between elements.
    
    Returns:
        List[int]: The modified list with delimeter inserted between elements.
    """
    if not numbers:
        return []
    
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(delimeter)
        result.append(numbers[i])
    
    return result

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter integer as input. It then iterates over the input list, appending the current element and the delimeter to the result list. If the input list is empty, it returns an empty list. The example usage demonstrates how to use this function with the provided test cases.