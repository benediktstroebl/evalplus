```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if not the last element
            result.append(delimeter)
    return result

# Example usage:
numbers = [1, 2, 3]
delimeter = 4
print(intersperse(numbers, delimeter))  # Output: [1, 4, 2, 4, 3]
```

This script uses a simple loop to iterate over the input list. For each number in the list, it appends the number to the result list, and then appends the delimeter if it is not the last element in the list.