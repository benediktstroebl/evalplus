```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): A list of integers.
    delimeter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
    List[int]: A new list with the delimeter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result


# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter as input, and returns a new list with the delimeter inserted between every two consecutive elements. The function uses a loop to iterate over the input list, appending each number and the delimeter (if not the last number) to the result list. The script also includes test cases to verify the function's correctness.