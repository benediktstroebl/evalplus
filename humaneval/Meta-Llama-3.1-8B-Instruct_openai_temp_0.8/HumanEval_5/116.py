```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between consecutive elements

    Returns:
        List[int]: The list with the delimeter inserted between consecutive elements
    """
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as arguments. It iterates over the input list, appending each element to the result list and the delimeter if the current index is not the last index in the list. The function then returns the resulting list with the delimeter inserted between consecutive elements. The provided test cases demonstrate the function's behavior with an empty list and a list with three elements.