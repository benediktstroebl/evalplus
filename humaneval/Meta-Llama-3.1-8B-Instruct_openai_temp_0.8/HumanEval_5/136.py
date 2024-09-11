```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The list of numbers to be interspersed.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The list with the delimiter inserted between elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if we are not at the last element
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4], 5))  # [1, 5, 2, 5, 3, 5, 4]
print(intersperse([10, 20, 30], 0))  # [10, 0, 20, 0, 30]
```

This script uses a simple loop to iterate over the input list. For each element, it appends the element to the result list, and then appends the delimiter if we are not at the last element in the list. The result list is then returned.