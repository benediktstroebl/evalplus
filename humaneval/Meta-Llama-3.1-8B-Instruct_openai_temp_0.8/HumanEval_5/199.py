```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between every two consecutive elements

    Returns:
        List[int]: The list with the delimeter inserted between every two consecutive elements

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the input list is empty, return an empty list
        return []

    result = [numbers[0]]  # Start with the first element of the list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.extend([delimeter, num])  # Insert the delimeter and the current number
    return result


# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that takes a list of integers and a delimeter integer as input, and returns a new list with the delimeter inserted between every two consecutive elements. The function iterates over the input list, inserting the delimeter and the current number at each step. If the input list is empty, the function returns an empty list. The script includes example usage at the end to demonstrate the function's behavior.