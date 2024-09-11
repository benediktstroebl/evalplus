```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    
    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between consecutive elements.
    
    Returns:
        List[int]: The modified list with the delimeter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Example use cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([5, 10, 15], 20))  # [5, 20, 10, 20, 15]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as input, and returns a new list with the delimeter inserted between every two consecutive elements of the input list. The function uses a simple loop to iterate over the input list, appending each element and the delimeter (if it's not the last element) to the result list. The example use cases demonstrate how to use this function with different input lists and delimeters.