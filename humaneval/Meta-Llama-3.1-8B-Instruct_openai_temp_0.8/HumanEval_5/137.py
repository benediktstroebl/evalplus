```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The delimiter number to insert between elements

    Returns:
        List[int]: The list with the delimiter inserted between elements
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Example usage
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function, which takes a list of integers `numbers` and an integer `delimeter` as input. It iterates over the input list, appending each element to the `result` list and then inserting the delimiter if it's not the last element in the list. Finally, it returns the modified list with the delimiter inserted between elements.