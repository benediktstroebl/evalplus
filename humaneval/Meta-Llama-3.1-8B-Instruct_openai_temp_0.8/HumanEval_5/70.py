```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between list elements

    Returns:
        List[int]: The list with the delimeter inserted between elements
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4], 5))  # [1, 5, 2, 5, 3, 5, 4]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter integer as input. It then iterates over the input list, appending each number and the delimeter (if it's not the last element) to the result list. The function finally returns the result list with the delimeter inserted between list elements. The test cases at the end demonstrate the function's behavior with different inputs.