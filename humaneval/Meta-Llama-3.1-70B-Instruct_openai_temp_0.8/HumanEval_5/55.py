```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with 'delimeter' inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        # Add the current number to the result
        result.append(num)
        # If it's not the last number in the list, add the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Example use cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([10, 20, 30, 40], 0))  # [10, 0, 20, 0, 30, 0, 40]
print(intersperse([5], 10))  # [5]
```