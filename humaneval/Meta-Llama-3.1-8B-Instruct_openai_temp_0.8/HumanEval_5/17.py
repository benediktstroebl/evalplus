```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): A list of integers
    delimeter (int): The number to be inserted between the list elements

    Returns:
    List[int]: The list with the specified delimeter inserted
    """
    result = []
    for i, n in enumerate(numbers):
        result.append(n)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result


# Example usage
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```