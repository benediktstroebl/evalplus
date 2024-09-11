```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted as a delimiter.

    Returns:
        List[int]: The modified list with the delimiter inserted.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = [numbers[0]]  # Start with the first element of the list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Append the delimiter
        result.append(num)  # Append the current number
    return result


# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```