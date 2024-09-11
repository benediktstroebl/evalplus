```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with 'delimeter' inserted between consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        # Add the current number to the result list
        result.append(num)
        
        # If it's not the last number, add the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    
    return result


# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```
This script defines the `intersperse` function that takes a list of integers and a delimeter as input, and returns a new list where the delimeter is inserted between every two consecutive elements. The function uses a simple loop to iterate over the input list, adding each number and the delimeter (if applicable) to the result list. The script also includes test cases to verify the function's correctness.